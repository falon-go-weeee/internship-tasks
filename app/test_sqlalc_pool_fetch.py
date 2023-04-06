from multiprocessing import Pool, cpu_count
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
from sqlalchemy.sql import func
from timed import timed

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
# define the query to execute
def process_row(row):
    print(row)
    # pass

@timed
def process_chunk(chunk):
    with engine.connect() as conn:
        query = select(products_table.c.id, products_table.c.gender, products_table.c.age_group, products_table.c.material, products_table.c.season, products_table.c.rating).where(products_table.c.id.between(chunk[0],chunk[1]))
        for row in conn.execute(query):
            process_row(row)

@timed
def multiprocess_query(table):
    with engine.connect() as conn:
        # divide the table into chunks by ID
        min_count = conn.execute(select(func.min(table.c.id))).scalar()
        # print(min_count)
        max_count = conn.execute(select(func.count(table.c.id))).scalar()
        # print(max_count)
        chunks = [(x, x + 100) for x in range(min_count, max_count, 100)]
        # print(chunks)
        process_count = cpu_count()
        # print("process_count :", process_count)
        with Pool(processes=process_count) as pool:
            pool.map(process_chunk, chunks)

if __name__ == '__main__':
    multiprocess_query(products_table)