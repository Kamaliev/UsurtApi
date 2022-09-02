from pydantic import BaseModel


class Info(BaseModel):
    time: str
    lessons: list[str]


class Item(BaseModel):
    items: list


if __name__ == '__main__':
    pass