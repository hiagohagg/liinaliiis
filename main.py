import click
from src.controllers.liinaliiis_controller import *

@click.group
def mycommands():
    pass

mycommands.add_command(liinaliiis)

if __name__ == '__main__':
    mycommands()