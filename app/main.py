from fastapi import FastAPI

from app.config.migrate import migrate_tables
from app.config.populate_db import populate_db
from app.modules.planting_area.planting_area_router import planting_area_router
from app.modules.rural_producer.rural_producer_router import \
    rural_producer_router
from app.modules.seed.seed_router import seed_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World 4"}


@app.post("/migrate")
async def migrate():
    await migrate_tables()
    return {"message": "Tables created"}


@app.post("/populate")
async def populate():
    await populate_db()
    return {"message": "Data populated"}

app.include_router(seed_router)
app.include_router(rural_producer_router)
app.include_router(planting_area_router)
