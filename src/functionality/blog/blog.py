from fastapi import Depends
from src.resource.blog import model
from src.resource.blog import schema
from sqlalchemy.orm import Session
from database import SessionLocal



def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


def create(request:schema.Blog, db :Session = Depends(get_db)):
    new_blog = model.Blog(title = request.title, body=request.body, name = request.name)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def all(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

def show(id,db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    return blog

def delete(id,db: Session = Depends(get_db)):
    db.query(model.Blog).filter(model.Blog.id == id).delete()
    db.commit()
    return "Done"

def uupdate(id, request: schema.Blog, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    

    blog.title = request.title
    blog.body = request.body
    blog.name = request.name

    db.commit()
    return "updated"