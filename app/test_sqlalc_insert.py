from multiprocessing import Pool
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String, CHAR, VARCHAR

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
products_table = Table('stores', metadata,
    Column('id', Integer, primary_key=True, autoincrement='auto'),
    Column('gender', String(10)),
    Column('age_group', String(10)),
    Column('material', String(50)),
    Column('season', String(10)),
    Column('rating', Integer)
)

metadata.create_all(engine)
# create a connection object
conn = engine.connect()

# create an insert statement
insert_statement = products_table.insert().values(gender='female', age_group='adult', material='cotton', season='summer', rating=4)

# execute the insert statement
result = conn.execute(insert_statement)
conn.commit()

# print the primary key of the inserted row
print(result.inserted_primary_key)
