import re
import codecs
import os
from os.path import join, dirname
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(name='DagApi',
      version=find_version('DAGAPI', '__init__.py'),
      description='Python API for work with Constellation Network',
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      keywords='Python API Constellation DAG',
      url='https://github.com/Pena-Co-Ltd/dag-api-python',
      author='Ivan Radaev',
      author_email='radaevir@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
          )