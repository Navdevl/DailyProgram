import pytest
from Programs import Tree

# Test Cases for Tree DS

def test_empty_node_value():
	with pytest.raises(TypeError):
		t = Tree()

def test_show_nodes():
	t = Tree(5)
	assert(t.printme==5)
