from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, join, CheckConstraint, ExceptionContext
from sqlalchemy.exc import DatabaseError

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

metadata = MetaData()

stores_table = Table('stores', metadata,
                    Column('id', Integer, primary_key=True, autoincrement='auto'),
                    Column('gender', String(10), nullable=False),
                    Column('age_group', String(10), nullable=False),
                    Column('material', String(50)),
                    Column('season', String(10)),
                    Column('rating', Integer,),
                    CheckConstraint('rating > 0', name='valid_rating')
                    )

addresses_table = Table('address', metadata,
                        Column('id', Integer, primary_key=True, autoincrement='auto'),
                        Column('address', String(50), nullable=False)
                        )

metadata.create_all(engine)

conn = engine.connect()

# CREATE TABLE address LIKE raw_addresses;
# INSERT INTO address SELECT * FROM raw_addresses

insert_in_stores = stores_table.insert().values(gender='female', age_group='adult', material='cotton', season='summer', rating=1)
insert_in_address = addresses_table.insert().values(address='950 MASON ST, SAN FRANCISCO, CA, 94108')

try:
    conn.execute(insert_in_stores)
    conn.execute(insert_in_address)
except DatabaseError as de:
    print('invalid_rating data', de._message())

conn.commit()
