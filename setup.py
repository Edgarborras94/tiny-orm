"""
Contains information necessaries to build, release and install a distribution.
"""
from setuptools import setup

setup(
    name='simple-orm',
    version='0.0.1',
    author='Meng Xiangzhuo',
    url='',
    license='MIT License',
    description='A simple ORM for SQLite',
    py_modules=['orm'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],  # see more at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    zip_safe=False
)
