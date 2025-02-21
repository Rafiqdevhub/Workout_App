from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_route
from routes import workout_route
from routes import routines_route
from api.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def read_root():
    return {"Hello Dear  world"}

app.include_router(auth_route.router)
app.include_router(workout_route.router)
app.include_router(routines_route.router)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)