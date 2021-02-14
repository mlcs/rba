from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rba',
    version='0.1.1',
    description=('Python toolbox for recurrence plot based analysis'),
    long_description=long_description,
    author='Bedartha Goswami',
    author_email='bedartha.goswami@uni-tuebingen.de',
    url='https://github.com/mlcs/rba',
    license='GNU Affero GPL v3.0',
    packages=['copra'],
#   no dependencies in this example
    install_requires=[
          'numpy',
          'pandas',
          'scipy',
         ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[ 
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: Only',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        ]
    )
