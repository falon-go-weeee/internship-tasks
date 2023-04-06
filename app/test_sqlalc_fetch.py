from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

user = 'root'
password = 'newpassword'
port = 3306
database = 'Akshay'
host = 'localhost'
# create an engine to connect to the database
sql_url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'
# print(sql_url)
engine = create_engine(sql_url)
print(engine)

# create a metadata object to hold information about the table
metadata = MetaData()

# define the table structure
products_table = Table('fashion_stores', metadata,
    Column('id', Integer, primary_key=True),
    Column('gender', String(10)),
    Column('age_group', String(10)),
    Column('material', String(50)),
    Column('season', String(10)),
    Column('rating', Integer)
)

# create a connection object
conn = engine.connect(engine)

# create a select statement
select_statement = select(products_table.c.id, products_table.c.gender, products_table.c.age_group, products_table.c.material, products_table.c.season, products_table.c.rating)
print(select_statement)
# execute the select statement
result = conn.execute(select_statement)

# fetch all the rows and print them
rows = result.fetchall()
print(rows)
for row in rows:
    print(row)
