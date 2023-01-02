""" Main Module for fastapi application """
import uvicorn

from fastapi import FastAPI
from routes import router as api_router

# from db import init_db


app = FastAPI()
app.include_router(api_router)


# @app.on_event('startup')
# async def on_start_up():
#     await init_db()


if __name__ == '__main__':
    uvicorn.run(app)
