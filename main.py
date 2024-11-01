from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog') #path
def index(limit=10, published:bool=True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from the database'}
    else:
        return{'data':f'{limit} blogs from the database'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id=id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments with id=id
    return {'data':{'1','2'}}