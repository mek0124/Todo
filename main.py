from app.commands.hello import hello
from app.commands.add_todo import add
from app.commands.list_todos import list
from app.commands.edit_todo import edit
from app.commands.delete_todo import delete

import click


@click.group()
def cli():
    pass


cli.add_command(hello)
cli.add_command(add)
cli.add_command(list)
cli.add_command(edit)
cli.add_command(delete)


if __name__ == '__main__':
    cli()