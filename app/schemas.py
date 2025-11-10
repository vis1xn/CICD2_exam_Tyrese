from typing import Annotated, Optional
from annotated_types import Ge, Le
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict

NameStr = Annotated[str, StringConstraints(min_length=1, max_length=100)]
Author_id = Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]
Book_id = Annotated[str, StringConstraints(pattern=r"^S\d{6}$")]
YearInt Annotated[int, Ge(1900), Le(2100)]
TitleStr = Annotated[str, StringConstraints(min_length=1, max_length=255)]
PagesInt = Annotated[int, Ge(1), Le(10000)]

class AuthorCreate(BaseModel):
    #AuthorDB
    name: NameStr
    email: EmailStr
    author_id: Author_id
    year: YearInt
    #BookDB
    book_id: Book_id
    title: TitleStr
    pages: PagesInt
