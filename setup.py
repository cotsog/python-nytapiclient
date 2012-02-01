from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nytapiclient',
      version=version,
      description="Python client for the New York Times API",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python nytimes api client',
      author='Dominic Jodoin',
      author_email='dominic.jodoin@gmail.com',
      url='http://cotsog.wordpress.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
