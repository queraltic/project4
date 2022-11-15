import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()

dbName = "df"
password= "root"

#os.getenv("sql_connection")


connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)