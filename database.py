from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db_url = "postgresql+psycopg2://postgres:Ay%40090405@localhost:5432/blogdb"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
