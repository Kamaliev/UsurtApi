import logging
import os.path
import sqlite3

logger = logging.getLogger(__name__)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.con = sqlite3.connect(os.path.abspath(r'E:\usurt_bot\db.sqlite3'), check_same_thread=False)

    def execute(self, query, *args):
        cursor = self.con.cursor()

        try:
            cursor.execute(query, args)
            self.con.commit()
        except sqlite3.Error as e:
            print(e)
            logger.error(e)
        finally:
            cursor.close()

    def get_result(self, query, *args):
        cursor = self.con.cursor()

        try:
            cursor.execute(query, args)
            return cursor.fetchone()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            cursor.close()

    def get_results(self, query, *args):
        cursor = self.con.cursor()

        try:
            cursor.execute(query, args)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            cursor.close()


if __name__ == '__main__':
    db = Database()
