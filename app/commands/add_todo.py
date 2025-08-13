from app.models.todo import TodoItemCreate, TodoItem
from app.controllers.json import JsonController

from datetime import datetime

import click


json_controller = JsonController()


@click.command()
@click.argument('title')
@click.argument('details')
@click.argument('priority')
def add(title: str, details: str, priority: int):
    current_todos = json_controller.get_todo_items()
    
    new_todo_item = TodoItemCreate(
        item_id = len(current_todos) + 1,
        title = title,
        details = details,
        priority = priority,
        created_at = str(datetime.now()),
        is_completed = False
    )

    did_save = json_controller.save_todo_item(new_todo_item.model_dump())

    click.echo("Todo Item Saved") if did_save else click.echo("Problem Saving Todo Item. See Console")
