from app.controllers.json import JsonController

import click


json_controller = JsonController()


@click.command()
@click.argument('item_id')
def delete(item_id: int) -> bool:
    currently_saved = json_controller.get_todo_items()
    updated_list = []

    for todo_item in currently_saved:
        if todo_item["item_id"] != int(item_id):
            updated_list.append(todo_item)

    did_save = json_controller.update_items(updated_list)

    click.echo("Todo Item Removed Successfully") if did_save else click.echo("There was an error removing the selected item and/or updating the database")
