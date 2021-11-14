import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

# these queries loads s3 data into redshift 
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

# these queries insert 
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn) # load s3 csv data into redshift 
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()