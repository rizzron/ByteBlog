from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(published: bool = True, limit: int = 10, sort: str | None = None):
    if published:
        return {'data': f'{limit} published blogs from the list'}
    else:
        return {'data': f'{limit} blogs from the list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': {id}}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: bool | None = None


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}
