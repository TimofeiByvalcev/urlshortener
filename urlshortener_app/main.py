import validators
from fastapi import FastAPI, HTTPException

from . import schemas

# Define app instantiating the FastAPI class

app = FastAPI()


# Use a path operation decorator to associate your root path with read_root() by registering it in FastAPI
@app.get("/")
def read_root():
    return "Welcome to the API of URL shortener"


# Define an exception if provided URL isn't valid
def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


# Define create_url endpoint which expects a URL string as POST request body
@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided url isn't valid")
    return f"TODO: Create db entry for : {url.target_url}"
