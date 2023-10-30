from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.users import user_router 

from models import connect_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
