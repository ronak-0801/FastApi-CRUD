from fastapi import FastAPI
from src.resource.blog.api import blog_route

app = FastAPI()

app.include_router(blog_route)