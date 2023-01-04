import click
from src.services.liinaliiis_service import *

@click.command()
@click.option("-a", "--alina", help="Recebe uma ordem.")
def liinaliiis(alina):
    try:
        command(alina)
    except:
        print("Error.")