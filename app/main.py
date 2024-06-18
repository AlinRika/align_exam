from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_tables, delete_tables
from app.logging_setup import logger
from app.routes import employees


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    logger.info("Database ready\n")
    yield
    await delete_tables()
    logger.info("Database clear\n\n")


# Initialize the app
app = FastAPI(lifespan=lifespan)

app.include_router(employees.router)
