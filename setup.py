from setuptools import setup, find_packages

setup(
	name = 'FixIt',
	packages = find_packages(exclude=['test']),
	entry_points={
	 'console_scripts':
	 ['fix = FixBraces.cli:fixing ',
	 'tree = FixBraces.cli:tree']

	},
	install_requires=(['click','pytest']),
	author = 'Naveen'

	)