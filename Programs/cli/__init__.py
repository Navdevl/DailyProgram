import click 
import pickle

from FixBraces import FixBraces as FB
from FixBraces import Tree

@click.command()
@click.option('-i', default=None, help='input query')
def fixing(i):
	f = FB(str(i))
	print f.fixing()


@click.command()
@click.option('-i', default=None, help='Insert into Node')
def tree(i):
	T = Tree(i)
	print "Give Negative Value to Stop Reading Inputs"
	data = 0
	while data >= 0:
		data = int(input())
		self.insert(data)

	print "Exited! Printing Tree,"
	T.printme(T)

