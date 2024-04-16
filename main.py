from fastapi import FastAPI , Depends
import schemas ,models
from database import engine , SessionLocal
from sqlalchemy.orm import Session
  
app = FastAPI()
 
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


  
models.Base.metadata.create_all(bind=engine)

@app.post('/blog',status_code=201)
def create(request:schemas.Blog, db :Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

@app.delete('/blog/{id}')
def delete(id,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()
    return "Done"

@app.put('/blog/{id}')
def uupdate(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    

    for key, value in request.dict().items():
        setattr(blog, key, value)

    db.commit()
    return "updated"