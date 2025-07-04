from dotenv import load_dotenv, find_dotenv
import os
from supabase import create_client

# Load .env
load_dotenv(find_dotenv())

# Debug: Print first 10 characters
print("URL:", os.getenv("SUPABASE_URL"))
print("Key:", os.getenv("SUPABASE_KEY")[:10], "…")

# Initialize Supabase client
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Query example
res = supabase.table("test_connection").select("*").execute()
print(res.data)
