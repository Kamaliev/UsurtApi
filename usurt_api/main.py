from fastapi import FastAPI
from api.endpoints import schedule, groups, auth
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(title='Usurt')

origins = [
    "*",
    'usurt.site'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(schedule.route)
app.include_router(groups.route)
app.include_router(auth.route)


if __name__ == '__main__':
    uvicorn.run(app)
