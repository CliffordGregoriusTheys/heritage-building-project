import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    sslmode="require"
)

with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM test_connection;")
        rows = cur.fetchall()
        print("Rows returned:", rows)

conn.close()
print("Connection closed.")
