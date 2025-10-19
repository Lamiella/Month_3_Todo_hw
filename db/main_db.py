import sqlite3
from db import queries
from config import path_db

# функция для создания БД
def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASK)
    conn.commit()
    conn.close()

# функция для добавления данных в БД
def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

# функция для получения данных из БД
def get_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASK)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# функция для обновления данных в БД
def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()

# функция для удаления данных в БД
def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id, ))
    conn.commit()
    conn.close()

# функция для удаления всех данных в БД
def del_all_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_ALL_TASK)
    conn.commit()
    conn.close()