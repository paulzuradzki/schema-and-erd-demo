# Demo: Schema Creation and Entity Relationship Diagramming

## Setup

Use Python 3.11. You may have dependency issues with pygraphviz library on 3.10.

```bash
# first, clone repo and navigate to root
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

```bash
python src/export_schema.py
```

This will create a directory '/out' and create 5 files.
* `erd.er`
* `erd.md`
* `erd.pdf`
* `schema.xlsx`
* `sql_ddl.sql`


## Terms
- `schema` - A general term for a specification of how data is or will be organized. A schema may also specify vocabulary, syntax, data types, attributes, value ranges, constraints, etc. SQLAlchmey uses the term [metadata](https://docs.sqlalchemy.org/en/20/glossary.html#term-metadata) in a similar sense as `schema`.
- `entity relationship model` - An [entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (or ER model) describes interrelated things of interest in a specific domain of knowledge. A basic ER model is composed of entity types (which classify the things of interest) and specifies relationships that can exist between entities (instances of those entity types).