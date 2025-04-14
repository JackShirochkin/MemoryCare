from pydantic import BaseModel, ConfigDict
from contextlib import asynccontextmanager 

class SLocationAdd(BaseModel):
   id_patient: int
   latitude: float
   longitude: float
   timestamp: str



class SLocation(SLocationAdd):
   id: int
   model_config = ConfigDict(from_attributes=True)

class SLocationId(BaseModel):
   id: int