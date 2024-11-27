from contextlib import asynccontextmanager

from fastapi import  FastAPI
from beanie import  init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from app.routes.bus_location_router import router as BusLocationRouter
from app.config.settings import settings
from app.models.bus_location import BusLocation

@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    app.db = AsyncIOMotorClient(settings.DB_URL).account  # type: ignore[attr-defined]
    await init_beanie(app.db, document_models=[BusLocation])
    app.include_router(BusLocationRouter)
    print("Startup complete")
    yield
    print("Shutdown complete")



app = FastAPI(
    title=settings.TITTLE,
    version=settings.VERSION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)