from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the API of URL shortener"