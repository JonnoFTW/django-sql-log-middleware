#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""django-sql-log-middleware - Write Django's SQL statements to a JSONL log file.
"""
from pathlib import Path

from setuptools import setup

version = '0.1.2'

setup(
    name='django-sql-log-middleware',
    version=version,
    packages=['django_sql_log_middleware'],
    install_requires=[
        'Django'
    ],
    long_description=Path('README.md', encoding='utf8').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/JonnoFTW/django-sql-log-middleware',
    license='MIT',
    author='JonnoFTW',
    author_email='jonmac1@gmail.com',
    description="Write Django's SQL statements to a JSONL log file",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ]
)
