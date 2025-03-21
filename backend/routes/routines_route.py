from fastapi import APIRouter 
from pydantic import BaseModel
from typing import Optional, List
from api.deps import db_dependency, user_dependency
from api.models import Routine, Workout
from sqlalchemy.orm import joinedload

router = APIRouter(
    prefix='/routines',
    tags=['routines']
)

class RoutineBase(BaseModel):
    name: str
    description: Optional[str] = None
    
class RoutineCreate(RoutineBase):
    workouts: List[int]=[]
    
    
    
@router.post("/")
def create_routine(db:db_dependency,user:user_dependency, routine: RoutineCreate):
    db_routine = Routine(name=routine.name, description=routine.description, user_id=user.get('id'))
    for workout_id in routine.workouts:
        workout = db.query(Workout).filter(Workout.id == workout_id).first()
        if workout:
            db_routine.workouts.append(workout)
    db.add(db_routine)
    db.commit()
    db.refresh(db_routine)
    db_routines = db.query(Routine).options(joinedload(Routine.workouts)).filter(Routine.id == db_routine.id).first()
    return db_routines

@router.get("/")
def get_routines(db:db_dependency, user:user_dependency):
    return db.query(Routine).options(joinedload(Routine.workouts)).filter(Routine.user_id == user.get('id')).all()

@router.delete("/{routine_id}")
def delete_routine(routine_id:int, db:db_dependency, user:user_dependency):
    db.query(Routine).filter(Routine.id == routine_id, Routine.user_id == user.get('id')).delete()
    db.commit()
    return {"message": "Routine Deleted"}