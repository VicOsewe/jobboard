
from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import List        
from fastapi import Depends,HTTPException,status

from pkg.infrastructure.db.session import get_db
from pkg.domain.dto.models.jobs import Job
from pkg.domain.dao.schemas.jobs import JobCreate,ShowJob
from pkg.infrastructure.db.repository.jobs import create_job, retreive_job,list_jobs, update_job_by_id,delete_job_by_id


router = APIRouter()

def create_new_job(job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    job = create_job(job=job,db=db,owner_id=current_user)
    return job


def read__new_job(id:int,db:Session = Depends(get_db)):
    job = retreive_job(id=id,db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with this id {id} does not exist")
    return job


def read_new_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs


def update_new_job(id: int,job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    message = update_job_by_id(id=id,job=job,db=db,owner_id=current_user)
    return message



def delete_new_job(id: int,db: Session = Depends(get_db)):
    current_user_id = 1
    message = delete_job_by_id(id=id,db=db,owner_id=current_user_id)
    return message