from fastapi import FastAPI
import os
app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": f"OK {os.getenv('SERVER_NAME')}"}
