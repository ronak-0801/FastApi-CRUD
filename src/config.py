#values that can't be share with anyone 

from dotenv import load_dotenv
import os


load_dotenv()


database_url = os.getenv("DATABASE_URL")
