from fastapi import FastAPI, Body
from requests import post

app = FastAPI()

@app.post('/')
async def send(req: dict=Body(...,embed=False)):
    post('http://46.8.69.112:8000/Telegram?key=DEFAULT', json=dict(req))
    return {'ok': True}