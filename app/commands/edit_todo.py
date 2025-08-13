

from app.controllers.json import JsonController
from app.models.todo import TodoItem

import click


json_controller = JsonController()


@click.command()
@click.argument('item_id')
@click.option('--title', help="The updated title of the todo item")
@click.option('--details', help="The updated details of the todo item")
@click.option('--priority', help="The updated priority of the todo item")
@click.option('--is_completed', help="The updated completion status of the todo item")
def edit(item_id: int, title: str = None, details: str = None, priority: int = None, is_completed: bool = None):
    if not title and not details and not priority and not is_completed:
        click.echo("No Changes Made")
        return

    found_todo_item = json_controller.get_todo_item(item_id)

    if not found_todo_item:
        click.echo(f"Error: No Todo Item Found By Item Id: {item_id}")
        return
    
    updated_todo_item = TodoItem(
        item_id = found_todo_item.item_id,
        title = title if title else found_todo_item.title,
        details = details if details else found_todo_item.details,
        priority = priority if priority else found_todo_item.priority,
        created_at = found_todo_item.created_at,
        is_completed = is_completed if is_completed else found_todo_item.is_completed,
    )
    
    did_update = json_controller.update_item(updated_todo_item)

    if not did_update:
        click.echo("There was a problem updating your entry")
        return
    
    click.echo(f"Entry {updated_todo_item.item_id} Has Been Updated Successfully")
