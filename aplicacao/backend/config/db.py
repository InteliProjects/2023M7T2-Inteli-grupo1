from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DB_USER = "postgres"
DB_PASSWORD = "yourpassword"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

session = Session(engine)

Base = declarative_base()