#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.0.1"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-germany-1822direkt',
      version=version,
      author="Mirko Dziadzka",
      author_email="mirko.dziadzka@gmail.com",
      url="https://github.com/kedder/ofxstatement",
      description=("ofxstatement plugin for Frankfurter Sparkasse / 1822direkt.com"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['germany_1822direkt = ofxstatement.plugins.germany_1822direkt:FrankfurterSparkasse1822Plugin']
          },
      install_requires=['ofxstatement'],
      include_package_data=True,
      zip_safe=True
      )