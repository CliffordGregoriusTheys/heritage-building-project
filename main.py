import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env into os.environ
load_dotenv()

# Initialize Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Run a simple query
resp = supabase.table("countries").select("*").execute()
print(resp.data)