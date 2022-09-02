from fastapi import APIRouter, Depends
from database import Schedule
from schema import groups
from .auth import auth

route = APIRouter(
)
db = Schedule()


@route.get('/groups/{facultative}/{course}', response_model=groups.Groups)
def get(facultative: str, course: int):
    result = db.get_groups(facultative, course)
    print(facultative, course)
    print(result.dict())
    return result


@route.get('/course/{facultative}')
def get_course(facultative: str):
    return dict(data=db.get_course(facultative))


@route.get('/facultative')
def get_facultatives():
    return dict(data=db.get_facultative())
