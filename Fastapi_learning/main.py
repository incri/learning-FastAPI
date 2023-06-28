from fastapi import FastAPI  #importing fastapi 

app = FastAPI()  # creating instance

@app.get('/') #decorating to indicate function
def index():    #creating function
    return {'Data' : {'Name' :'Anoj'}}


@app.get('/about')
def about():
    return {'Data':'About Page'}