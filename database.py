from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
   pass

class TaskOrm(Model):
   __tablename__ = "tasks"
   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str]
   description: Mapped[str | None]



class Model(DeclarativeBase):
   pass

class TaskOrm(Model):
   __tablename__ = "locations"
   id: Mapped[int] = mapped_column(primary_key=True)
   id_patient: Mapped[int]
   latitude: Mapped[float]
   longitude: Mapped[float]
   timestamp: Mapped[str]

async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)
async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)