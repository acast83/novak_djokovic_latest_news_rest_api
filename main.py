from fastapi import FastAPI
from blic_data import blic_dict
from mondo_data import mondo_dict
app = FastAPI()

@app.get("/")
def root():
    return{"Welcome":"to my Novak Djokovic news API"}

@app.get("/api")
async def news_api():
    
    return {"Blic":blic_dict,"Mondo":mondo_dict}
