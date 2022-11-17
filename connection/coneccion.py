import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
database = os.getenv('DB')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

#conn = psycopg2.connect(host=host,database=database,user=user,password =password)

print(host)