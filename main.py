from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "world"} 
# JSON response => {"Hello" : "world"}


# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
# Below here, q variable will be interpreted as query string parameter eg: http://localhost:8000/items?q=yo
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) :
    return {
        "item_id": item_id,
        "q": q
    }



# You may have installed Python packages into your global environment, which can cause conflicts between package versions. Would you like to create a virtual environment with these packages to isolate your dependencies?