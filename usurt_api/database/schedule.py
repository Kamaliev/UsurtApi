from database import Database
from schema import Groups


class Schedule:
    def __init__(self):
        self.__db = Database()

    def get_schedule(self, group_name: str, odd: int):
        query = "select day, time, desc from Schedule where group_name = ? and odd = ?"
        data = self.__db.get_results(query, group_name, odd)
        return data

    def get_groups(self, facultative, course):
        query = '''select distinct(group_name) from Schedule where facultative_id = (select id from Facultative where name = ? and course = ?)'''
        result = [i[0] for i in self.__db.get_results(query, facultative, course)]
        return Groups(data=result)

    def get_facultative(self):
        query = '''select distinct(name) from Facultative'''
        result = [i[0] for i in self.__db.get_results(query)]
        return result

    def get_course(self, facultative):
        query = '''select distinct(course) from Facultative where name = ? and id in (select distinct(facultative_id) from Schedule)'''
        result = [i[0] for i in self.__db.get_results(query, facultative)]
        return result


if __name__ == '__main__':
    db = Schedule()
    res = db.get_schedule('ИТси-111', 0)
    # print(res.dict())
    for i in res.items:
        print(i.info)
        for row in i.data:
            print(row)
