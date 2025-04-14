from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import SLocationAdd, SLocation

class LocationRepository:
   @classmethod
   async def add_location(cls, location: SLocationAdd) -> int:
       async with new_session() as session:
           data = location.model_dump()
           new_location = TaskOrm(**data)
           session.add(new_location)
           await session.flush()
           await session.commit()
           return new_location.id

   @classmethod
   async def get_locations(cls) -> list[SLocation]:
       async with new_session() as session:
           query = select(TaskOrm)
           result = await session.execute(query)
           location_models = result.scalars().all()
           locations = [SLocation.model_validate(location_model) for location_model in location_models]
           return locations
"""""
   @classmethod
   async def get_location_by_id(cls, id_patient_requested: int) -> SLocation:
       async with new_session() as session:
           query = select(TaskOrm).where(TaskOrm.id_patient.in_(id_patient_requested)).order_by(TaskOrm.id.desc()).first()
           result = await session.execute(query)
           location_by_selected_id = result.scalars().first()
           location = SLocation.model_validate(location_by_selected_id)
           return location 

"""
    




  
       
       
       