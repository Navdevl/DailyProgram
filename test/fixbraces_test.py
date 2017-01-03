import pytest

from Programs import FixBraces

# Test cases for FixBraces

def test_trailing_braces():
	f = FixBraces('ab()()')
	assert(f.fixing() == 'ab')

def test_for_no_input():
	with pytest.raises(TypeError):
		f = FixBraces()

def test_for_string_output():
	f = FixBraces('abcd()')
	assert(type(f.fixing()) == str)