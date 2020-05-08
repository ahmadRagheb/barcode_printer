# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in barcode_printer/__init__.py
from barcode_printer import __version__ as version

setup(
	name='barcode_printer',
	version=version,
	description='Barcode Printer App To Print Serial No. as Barcode',
	author='Abdullah Zaqout',
	author_email='zaqoutabed@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
