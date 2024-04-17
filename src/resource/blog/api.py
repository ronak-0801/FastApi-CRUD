from fastapi import  APIRouter, Depends
from src.resource.blog import model
from src.resource.blog import schema
from sqlalchemy.orm import Session
from database import engine , SessionLocal


from src.functionality.blog.blog import create, all,show,delete,uupdate

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()
  
blog_route = APIRouter()
 
model.Base.metadata.create_all(bind=engine)

@blog_route.post('/blog')
def create_blog(request:schema.Blog, db :Session = Depends(get_db)):
    return create(request,db)

@blog_route.get("/blog")
def show_all(db: Session = Depends(get_db)):
    return all(db)

@blog_route.get('/blog/{id}')
def read(id,db: Session = Depends(get_db)):
    return show(id,db) 


@blog_route.delete('/blog/{id}')
def dele(id,db: Session = Depends(get_db)):
    return delete(id,db)

@blog_route.put('/blog/{id}')
def up(id, request: schema.Blog, db: Session = Depends(get_db)):
    return uupdate(id,request,db)
