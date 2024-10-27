from fastapi import FastAPI


app = FastAPI()


@app.get('/') #path
def index():
    return {'data':'blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id:int):
    #fetch blog with id=id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments with id=id
    return {'data':{'1','2'}}