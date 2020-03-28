from setuptools import setup, find_packages

setup(
	name='madh',
	version='1.0.0',
	description='Math Learning Notebooks for Digital Humanities students',
	packages=find_packages('src'),
	package_dir={'':'src'}
	)