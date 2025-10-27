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
def get_tasks(filter_type='all'):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_TASKS_COMPLETED)
    elif filter_type == "uncompleted":
        cursor.execute(queries.SELECT_TASKS_UNCOMPLETED)
    else:
        cursor.execute(queries.SELECT_TASK)

    tasks = cursor.fetchall()
    conn.close()
    return tasks

# функция для обновления данных в БД
def update_task(task_id, new_task=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute(queries.UPDATE_TASK, (new_task, task_id))

    if completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))

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

def del_completed():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_COMPLETED)
    conn.commit()
    conn.close()