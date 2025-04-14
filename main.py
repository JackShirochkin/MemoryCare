from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from schemas import SLocationAdd, SLocation
from fastapi import Depends
from router import router as locations_router

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")



app = FastAPI(lifespan=lifespan)
app.include_router(locations_router)
@app.get("/")
async def home(latitude: float, longitude: float):
   latitude_str = str(latitude)
   longitude_str = str(longitude)
   summary = "latitude: " + latitude_str + ", longitude: " + longitude_str
   return {"data": summary}



