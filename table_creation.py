import configparser # grabbing the values in a config file 
import psycopg2 # for connecting to database
from table_queries import create_table_queries, drop_table_queries

def drop_tables(cur,conn):
    for query in drop_table_queries: # each element in drop_table_queries is a query that drops each corresponding table
        cur.execute(query)
        conn.commit() # need to do this at every query done
        
def create_tables():
    for query in create_table_queries: # each element in create_table_queries is a query that drops each corresponding table
        cur.execute(query)
        conn.commit() # need to do this at every query done

def main():
    # grabbing the credentials we need to connect to data warehouse(redshift) 
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # creating a connection to data warehouse(redshift) 
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values())) # *config - this uses unpacking which means grab all of the element inside the array and pass them one by one 
    cur = conn.cursor() # used for creating queries 

    # creating tables for the schema of data warehouse(redshift)
    drop_tables(cur,conn) # yep we drop them first so we're sure the tables we're creating are fresh 
    create_tables(cur,conn)

    # close connection to database
    conn.close()

main()
