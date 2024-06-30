from typing import Annotated
from fastapi import Depends, FastAPI
from starlette.config import Config
from sqlmodel import SQLModel, create_engine, Session
try:
    config = Config(".env")
    
except FileNotFoundError as error:
    print(error)
    

db = config("DB")


connection_string = db.replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string, pool_pre_ping=True, echo=True
)

def get_session():
    with Session(engine) as session:
        yield session

DB_SESSION = Annotated[Session, Depends(get_session)]

async def create_db_and_tables(app: FastAPI):
    print(f"creating tables... {app}")
    SQLModel.metadata.create_all(engine)
    yield