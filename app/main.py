# app/main.py
from typing import Optional

from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import engine, SessionLocal
from app.models import Base
#from app.schemas import 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (dev/exam). Prefer Alembic in production.
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()


# ---- Health ----
@app.get("/health")
def health():
    return {"status": "ok"}

#---- Authors ----
@app.post("/api/user", response_model = AuthorRead, status_code = status.HTTPException_201_CREATED)
def add_author(payload: AuthorCreate, db: Session = Depends(get_db))
author = AuthorDB(**payload.model_dump())
db.add(author)
    try:
        db.commit
        db.refresh(author)
    except IntegrityError
        db.rollback()
        raise HTTPException(status_code=409, details-"Author already exists")
    return author

@app.get("/api/author/{author_id}", response_model = AuthorRead)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.get(AuthorDB, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.put("/api/author/{author_id}", response_model = AuthorRead, status_code = 200) 
def update_author(author_id: int, payload: AuthorRead, db: Session = Depends(get_db)):
    author = AuthorDB(**payload.model_dump())
    try:
        stmt = update(AuthorDB).where(AuthorDB.id == author_id).values(id = author.id, name = author.name, email = author.email, year = author.year)
        db.execute(stmt)
        db.commit()
        except IntegrityError:
            db.rollback
        raise HTTPException(status_code=409, detail="Author already exists")
        return author

@app.patch("/api/author/{author_id}", response_model = AuthorPATCH, status_code.HTTPException_201_CREATED) 
def patch_author(author_id: int, payload: AuthorPATCH, db: Session = Depends(get_db)):
  if not author:
        raise HTTPException(status_code=404, detail="No new details")
    try:
        stmt = update(AuthorDB).where(AuthorDB.id == author_id).values(**author_details)
        db.execute(stmt)
        db.commit()
    except IntegrityError:
            db.rollback
        raise HTTPException(status_code=409, detail="Author already exists")
    return author_details

@app.delete("/api/author/{author_id}", status_code=204)
def delete_author(author_id: int db : Session = Depends(get_db)) Response:
    author = db.get(AuthorDB, author_id)
     if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return Response(status_code=status.HTTPException_204_NO_CONTENT)

