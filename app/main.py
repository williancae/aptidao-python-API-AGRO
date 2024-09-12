from fastapi import FastAPI

from app.modules.planting_area.planting_area_router import planting_area_router
from app.modules.rural_producer.rural_producer_router import \
    rural_producer_router
from app.modules.seed.seed_router import seed_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World 4"}


app.include_router(seed_router)
app.include_router(rural_producer_router)
app.include_router(planting_area_router)
