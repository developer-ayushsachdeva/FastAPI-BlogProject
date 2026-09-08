from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine,SessionLocal
import model,Schemas
from auth import create_access_token, verify_access_token, oauth2_scheme

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Login endpoint
@app.post("/login")
def login(form_data: Schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
def root():
    return {"message": "Blog API is running"}

@app.post("/blogs", response_model=Schemas.BlogResponse)
def create_blog(blog: Schemas.BlogCreate, db: Session = Depends(get_db),user: dict = Depends(verify_access_token)):
    new_blog = model.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs", response_model=list[Schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(model.Blog).all()

@app.get("/blogs/{blog_id}", response_model=Schemas.BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.put("/blogs/{blog_id}", response_model=Schemas.BlogResponse)
def update_blog(blog_id: int, blog: Schemas.BlogCreate, db: Session = Depends(get_db),user: dict = Depends(verify_access_token)):
    existing_blog = db.query(model.Blog).filter(model.Blog.id == blog_id).first()
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    existing_blog.title = blog.title
    existing_blog.body = blog.body
    db.commit()
    db.refresh(existing_blog)
    return existing_blog

@app.delete("/blogs/{blog_id}")
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verify_access_token)
):
    existing_blog = db.query(model.Blog).filter(model.Blog.id == blog_id).first()
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(existing_blog)
    db.commit()
    return {"message": "Blog deleted successfully"}