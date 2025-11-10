from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint

class Base(DeclarativeBase):
    pass

class AuthorDB(Base):
    __tablename__="authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    year_started: Mapped[int] = mapped_column(Integer, nullable=False)
    author_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    books: Mapped[list["BookDB"]] = relationship(back_populates = "authors", cascade = "all, delete_orphan")

class BookDB(Base):
    __tablename__="books"
    id: Mapped[int] = mapped_column(primary_key=True)    
    title: Mapped[str] = mapped_columnn(String(255), nullable=False)
    pages: Mapped[int] = mapped_column(Integer, nullable=False)
    book_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete = "CASCADE"), nullable=False)
    author: Mapped["AuthorDB"] = relationship(back_populates ="books")


