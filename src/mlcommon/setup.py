#!/usr/bin/env python

from distutils.core import setup

setup(name='Machine Learning Common Files',
      version='1.0',
      description='Useful modules for Machine Learning projects',
      author='GrupoML',
      author_email='tferrer@itba.edu.ar',
      url='http://www.tferrer.net.ar/',
      packages=['mlmetrics'],
      install_requires=['numpy', 'matplotlib'],
     )