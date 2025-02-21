from fastapi import APIRouter , status
from api.models import Workout
from typing import Optional
from api.deps import db_dependency, user_dependency
from pydantic import BaseModel


router = APIRouter(
    prefix='/workout',
    tags=['workout']
)

class WorkoutBase(BaseModel):
    name: str
    description: Optional[str] = None

   
class WorkoutCreate(WorkoutBase):
    pass

@router.post("/")
def create_workout(db: db_dependency, user:user_dependency, workout: WorkoutCreate):
    db_workout = Workout(**workout.model_dump(), user_id=user.get("id"))
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

@router.get("/workouts")
def get_workouts(db: db_dependency, user:user_dependency):
    return db.query(Workout).filter(Workout.user_id == user.get("id")).all()

@router.get("/{workout_id}")
def get_workout(workout_id: int, db: db_dependency, user:user_dependency):
    return db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == user.get("id")).first()

@router.delete("/{workout_id}")
def delete_workout(workout_id: int, db: db_dependency, user:user_dependency):
    db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == user.get("id")).delete()
    db.commit()
    return {"message": "Workout Deleted"}