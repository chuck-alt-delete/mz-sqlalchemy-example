from sqlalchemy.orm import Session
from sqlalchemy import select
from config import engine
from models import T


statement = select(T).where(T.id.between(0,5))

with Session(engine) as session:
    for row in session.scalars(statement=statement):
        print(row)

