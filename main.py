from model import model_pipeline
# imports model_pipeline function from model.py file
from fastapi import FastAPI,  UploadFile
from typing import Union
import io
from PIL import Image
#The Union type is used for indicating that a function argument, return type, or variable could be one of multiple specified types.

app = FastAPI()         # an instance of fastapi class.

# # this is whenever someone uses HTTP GET request and it goes to the root route ("/") then below function shall be used to handle that request. 
# @app.get("/")   # it is a decorater, which is basically, do your thing with the thing that you have below.

# # here item_id is a path parameter. fastapi automatically extracts suppose 5 if the route is /items/5 .
# @app.get("/items/{item_id}")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    # image = Image.open(image.file)
    
    result = model_pipeline(text, image)
    return {"answer": result}