import flet as ft
from db import main_db
from datetime import datetime as dt

def main(page: ft.Page):
    page.title = 'ToDo list'
    page.theme_mode = ft.ThemeMode.DARK

    task_list = ft.Column(spacing = 10)

    def create_task_row(task_id, task_text):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)
        time_now = dt.now()
        time = time_now.strftime('%Y-%m-%d %H:%M:%S')
        task_time = ft.Text(value=time)

        def enable_edit(_):
            task_field.read_only = False
            task_field.on_submit = save_edit
            task_field.update()
        
        def save_edit(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            new_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
            task_time.value = new_time
            task_time.update()
            task_field.update()
            page.update()
        
        def del_task(_):
            main_db.delete_task(task_id)
            load_task()

        enable_button = ft.IconButton(icon=ft.Icons.EDIT, tooltip='Редактировать', on_click=enable_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE_ALT_ROUNDED, on_click=save_edit)
        del_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=del_task, icon_color=ft.Colors.RED)

        return ft.Row([task_time, task_field, enable_button,save_button, del_button])
    
    def load_task():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task_text))
        page.update()
    
    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task))
            task_input.value = ''
            page.update()

    def del_all(_):
            main_db.del_all_tasks()
            load_task()

    del_all_button = ft.ElevatedButton('Удалить все задачи', on_click=del_all)
    task_input = ft.TextField(label='Введите задачу', expand=True, on_submit=add_task)
    add_button = ft.IconButton(icon=ft.Icons.ADD, tooltip= 'Добавить задачу',on_click=add_task)
    
    page.add(ft.Row([task_input,add_button]),task_list, 
             ft.Row([del_all_button], alignment=ft.MainAxisAlignment.END))

    load_task()

if __name__  == '__main__':
    main_db.init_db()
    ft.app(target = main)