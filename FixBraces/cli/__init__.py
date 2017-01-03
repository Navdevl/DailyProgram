import click 

from FixBraces import FixBraces as FB
from FixBraces import Tree

@click.command()
@click.option('-i',default=None, help='input query')
def fixing(i):
	f = FB(str(i))
	f.fixing()


@click.command()
@click.option('-i',default=None,help='Insert into Node')
def tree(i):
	T = Tree(i)
	T.get_input()
	T.printme(T)

