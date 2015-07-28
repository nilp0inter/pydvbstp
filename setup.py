# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGELOG = open(os.path.join(HERE, 'CHANGELOG.rst')).read()

VERSION = '0.0.1'

setup(name='pydvbstp',
      version=VERSION,
      description="DVBSTP protocol for Python",
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
      ],
      keywords='DVBSTP',
      author='Roberto Abdelkader Martínez Pérez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/nilp0inter/pydvbstp',
      license='LGPLv3',
      packages=find_packages(exclude=["tests", "docs"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'bitstring==3.1.3',
          'attrs==15.0.0'
      ],
      entry_points={
      })
