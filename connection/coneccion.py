import psycopg2;
import os;
from dotenv import load_dotenv;

load_dotenv()

conn = psycopg2.connect(    
    host = os.getenv('HOST'),
    database = os.getenv('DB'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'))
