import logging

from fastapi import APIRouter, Depends
from database import Schedule
from schema import schedule as model
from .auth import auth

route = APIRouter(prefix='/schedule')
db = Schedule()

week = [
    'time',
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье',
]


@route.get('/{group_name}/{odd}', response_model=model.Item)
def get(group_name: str, odd: int):
    schedules = db.get_schedule(group_name, odd)
    times = sorted(set([row[1] for row in schedules]))
    result = {i: [model.Info(time=j, lessons=[]) for j in times] for i in week}
    for row in schedules:
        day, time, desc = row
        for item in result[day]:
            if item.time == time:
                item.lessons += [desc]

    result['time'] = [model.Info(time=i, lessons=[i]) for i in times]
    return model.Item(items=list(result.values()))


if __name__ == '__main__':
    data = get('ПСгв-121', 0)
    for i in data.items:
        for j in i:
            print(j.time)
            for lesson in j.lessons:
                print(lesson)
    data = db.get_schedule('ПСгв-121', 0)
    # print(data)
