from fastapi import FastAPI

from app.modules.seed.seed_router import seed_router

app = FastAPI()

# Now include the router after it's defined correctly
app.include_router(seed_router)


@app.get("/")
def read_root():
    return {"message": "Hello World 4"}
