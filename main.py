from typing import List
from fastapi import FastAPI, Depends
from pydantic import json
from fastapi.encoders import jsonable_encoder
import edgedb, uuid

app = FastAPI()

# DB Dependency
async def get_db():
    db : edgedb.asyncio_client.AsyncIOClient = edgedb.asyncio_client.create_async_client(database='edgedb',user='edgedb', host='edgedb', port=5656, tls_security="insecure")
    try:
        yield db
    finally:
         await db.aclose()

def encode_obj(obj):
    answer = {}
    for attr in dir(obj):
        val = getattr(obj, attr)
        answer[attr] = jsonable_encoder(val)
    return answer

def encode_set(obj):
    answer = [jsonable_encoder(x) for x in obj]
    return answer

json.ENCODERS_BY_TYPE[uuid.UUID] =  lambda obj: str(obj)   
json.ENCODERS_BY_TYPE[edgedb.Set] =  encode_set
json.ENCODERS_BY_TYPE[edgedb.Object] = encode_obj


@app.get("/") 
async def get_persons(edb : edgedb.asyncio_client.AsyncIOClient = Depends(get_db)):

    users = edgedb.Object = await edb.query('SELECT Person {first_name}')
    return users


@app.put("/") 
async def create_person(first_name:str, last_name:str, edb : edgedb.asyncio_client.AsyncIOClient = Depends(get_db)):

    return await edb.query("""
        INSERT Person {
            first_name := <str>$first_name,
            last_name := <str>$last_name
        }
    """, first_name=first_name, last_name=last_name)
