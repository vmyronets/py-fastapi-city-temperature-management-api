from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from temperatures.router import router as temp_router
from cities.router import router as city_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(temp_router)
app.include_router(city_router)


@app.get("/")
async def root() -> dict:
    return {"message": "City and Temperature API"}
