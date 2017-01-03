from setuptools import setup, find_packages

setup(
	name = 'FixIt',
	packages = find_packages(exclude=['test']),
	entry_points={
	 'console_scripts':
	 ['fix = FixBraces.cli:fixing ']

	},
	install_requires=(['click','pytest']),
	author = 'Naveen'

	)