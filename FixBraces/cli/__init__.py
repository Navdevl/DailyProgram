import click 

from FixBraces import FixBraces as FB

@click.command()
@click.option('-i',default=None, help='input query')
def fixing(i):
	f = FB(str(i))
	f.fixing()