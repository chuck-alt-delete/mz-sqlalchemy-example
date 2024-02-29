from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class T(Base):
    __tablename__ = 't'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    def __repr__(self) -> str:
        return f'ID: {self.id!r}\nContent: {self.content!r}\n\n'