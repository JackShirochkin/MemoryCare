from fastapi import APIRouter
from repository import LocationRepository
from schemas import SLocation, SLocationAdd, SLocationId
from fastapi import Depends

router = APIRouter(
   prefix="/locations",
   tags=["Местоположения"],
)




@router.post("")
async def add_location(location: SLocationAdd = Depends()) -> SLocationId:
   new_location_id = await LocationRepository.add_location(location)
   return {"id": new_location_id}

@router.get("")
async def get_locations() -> list[SLocation]:
   locations = await LocationRepository.get_locations()
   return locations


#@router.get("")
#async def get_location_by_id(id_patient_requested : int = Depends()) -> SLocation:
#   location = await LocationRepository.get_location_by_id(id_patient_requested)
#   return location