from fastapi import FastAPI


app = FastAPI()
@app.get("/")

async def home(latitude: float, longitude: float):
   latitude_str = str(latitude)
   longitude_str = str(longitude)
   summary = "latitude: " + latitude_str + ", longitude: " + longitude_str
   return {"data": summary}