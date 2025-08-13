from app.controllers.json import JsonController
from app.models.todo import TodoItem
import click

json_controller = JsonController()

@click.command()
@click.option("--item_id", type=int, help="Filter items by specific ID")
def list(item_id):
    """List all todo items or filter by specific ID"""
    all_items = json_controller.get_todo_items()

    if not all_items:
        click.echo("No Todo Items Found")
        return

    if item_id is not None:
        all_items = [item for item in all_items if item["item_id"] == item_id]
        if not all_items:
            click.echo(f"No item found with ID: {item_id}")
            return

    for item_data in all_items:
        item = TodoItem(**item_data)
        click.echo("-" * 30)
        click.echo(f"""
ID: {item.item_id}
Title: {item.title}
Details: {item.details}
Priority: {item.priority}
Created At: {item.created_at}
Completed: {"Yes" if item.is_completed else "No"}
""")
    
    click.echo("-" * 30)