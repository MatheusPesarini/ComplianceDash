from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

# class User(Base):
#     __tablename__ = "users"
    
#     id: 