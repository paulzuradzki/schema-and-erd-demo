from io import StringIO
from pathlib import Path

import pandas as pd
from eralchemy2 import render_er
from models import metadata_obj
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable


def main():
    output_dir = Path("out")
    output_dir.mkdir(exist_ok=True)
    output_filepath_schema = output_dir / "schema.csv"
    output_filepath_sql = output_dir / "sql_ddl.sql"
    export_schema_table(metadata_obj, output_filepath_schema)
    export_sql_ddl(metadata_obj, output_filepath_sql)
    export_erd_files(metadata_obj, output_dir)

def export_erd_files(metadata_obj, output_dir):

    output_filepath_erd_pdf = output_dir / "erd.pdf"
    output_filepath_erd_er = output_dir / "erd.er"
    output_filepath_erd_md = output_dir / "erd.md"

    erd_filepaths = [
        output_filepath_erd_pdf,
        output_filepath_erd_er,
        output_filepath_erd_md,
    ]

    for erd_filepath in erd_filepaths:
        render_er(metadata_obj, str(erd_filepath))


def export_schema_table(metadata_obj, output_filepath_csv):
    """Script to create an Excel workbook with a table showing column-level DB schema.

    This includes table names, column names, types, and comments.
    """

    column_items = []
    for table_name, table in metadata_obj.tables.items():
        for column in table.columns:
            column_item = {
                "table_name": table_name,
                "column.name": column.name,
                "column.type": column.type,
                "column.primary_key": column.primary_key,
                "column.foreign_keys": ", ".join(
                    [
                        f"{k.column.table.name}.{k.column.name}"
                        for k in column.foreign_keys
                    ]
                ),
                "column.nullable": column.nullable,
                # Description of column
                "column_comment": column.comment,
                # Description of table
                "table_comment": table.comment,
            }
            column_items.append(column_item)

    schema_df = pd.DataFrame(column_items)
    schema_df.to_csv(output_filepath_csv, index=False)

def export_sql_ddl(metadata_obj, output_filepath):

    # Create an engine for SQLite in memory (you can choose other engines too)
    engine = create_engine('sqlite:///:memory:')

    # Use StringIO to capture the SQL output
    sio = StringIO()
    with engine.connect() as conn:
        for table in metadata_obj.sorted_tables:
            sio.write(str(CreateTable(table).compile(conn)) + ";\n")

    sql_ddl_string = sio.getvalue()
    with open(output_filepath, "w") as f:
        f.write(sql_ddl_string)

if __name__ == "__main__":
    main()
