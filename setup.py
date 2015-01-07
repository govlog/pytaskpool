# coding=utf-8

"""
Setup file for pytaskpool
"""

from setuptools import setup, find_packages, Command
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        errno = subprocess.call([sys.executable, 'runtests.py', '-v'])
        raise SystemExit(errno)


setup(
    name='pytaskpool',
    version='1.0b4',

    description='A simple multiprocessing function pool',
    long_description=long_description,

    author='AMIAUD Christopher',
    author_email='christopher.amiaud@gmail.com',

    url='https://github.com/govlog/pytaskpool',
    download_url='https://github.com/govlog/pytaskpool/tarball/1.04b',

    license='GPL',

    classifiers=[

        'Development Status :: 4 - Beta',

        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',

        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System :: Hardware :: Symmetric Multi-processing',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',

    ],

    keywords='simple multiprocessing function pool',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['multiprocessing'],

    cmdclass={'test': PyTest}


)