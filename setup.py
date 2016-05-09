# coding: utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

readme = open('README').read()

setup(
    name='essay_demo_webpy',
    version='${version}',
    description=readme.partition('\n')[0],
    long_description=readme,
    author='wap-tech',
    author_email='mpcyd@sohu-inc.com',
    url='http://read.sohu.com',
    packages=find_packages(exclude=['*.pyc']),
    include_package_data=True,
    package_data={
    },
    install_requires=[
        "web.py",
    ],
    entry_points={
        'console_scripts': [
            'essay_demo_webpy = essay_demo_webpy.main:main',
        ]
    },
)
