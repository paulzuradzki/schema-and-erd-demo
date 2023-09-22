from sqlalchemy import (
    BOOLEAN,
    DATE,
    DECIMAL,
    TEXT,
    TIMESTAMP,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    text,
)

metadata_obj = MetaData()

fact_orders = Table(
    "fact_orders",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),  
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),  
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),  
    Column(
        "dim_customer_id",
        Integer,
        ForeignKey("dim_customer.id"),
        comment="Customer ID for joining to customer dimensions.",
    ),  
    Column(
        "dim_product_id",
        Integer,
        ForeignKey("dim_product.id"),
        comment="Product ID for joining to Product dimensions.",
    ),  
    Column(
        "dim_discount_type_id",
        Integer,
        ForeignKey("dim_discount_type.id"),
        comment="Discount type ID for joining to discount description dimension.",
    ),  
    Column("sale_date", DATE, comment="Date of sale."),
    Column("sale_qty", DECIMAL, comment="Sale quantity."),
    Column("sale_amount", DECIMAL, comment="Purchase price amount."),
    comment="Order transactions table to caputure the event of a product sale and measures like purchase price amount.",  
)

fact_customer_relations = Table(
    "fact_customer_relations",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),
    Column(
        "dim_customer_id",
        Integer,
        ForeignKey("dim_customer.id"),
        comment="Customer ID for joining to customer dimension.",
    ),
    Column("encounter_date", DATE, comment="Date of customer encounter."),
    Column(
        "encounter_notes",
        TEXT,
        comment="Notes for a given encounter with a customer.",
    ),
    Column(
        "is_repeat_customer",
        BOOLEAN,
        comment="True if customer is a repeat customer. Otherwise, False.",
    ),     
    comment="Track customer relation encounters and notes. An individual customer may have multiple notes and encounters.",  # noqa
)

dim_customer = Table(
    "dim_customer",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),
    Column("first_name", String(50), comment="Customer first name."),
    Column("last_name", String(50), comment="Customer last name."),
    Column("middle_initial", String(10), comment="Customer middle initial."),
    Column("address", String(100), comment="Customer street address."),
    Column("city", String(100), comment="Customer address city."),
    Column("state", String(100), comment="Customer address state."),
    Column("country", String(100), comment="Customer address country."),
    comment="Customer dimension table.",
)

DISCOUNT_TYPE_CHOICES = [
    "N/A",
    "EndofYear",
    "Repeat Customer",
    "Senior Citizen",
]
dim_discount_type = Table(
    "dim_discount_type",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),  
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),  
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),  
    Column(
        "name",
        String(20),
        comment=f"Description of discount type. Constrained to {','.join(DISCOUNT_TYPE_CHOICES)}.", # noqa
    ),  
    CheckConstraint(
        f"name IN {tuple(DISCOUNT_TYPE_CHOICES)}", name="valid_discount_type"
    ),
    comment="Discount type mapping table.",  
)

dim_product = Table(
    "dim_product",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),  
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),  
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),  
    Column(
        "name",
        String(100),
        comment="Product name (short description).",
    ),  
    Column(
        "description_long",
        Text(),
        comment="Product long description.",
    ),      
    comment="Directory listing of Products."
)
