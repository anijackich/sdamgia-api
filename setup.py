# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='sdamgia-api',
    version='0.1.5',
    author='anijack',
    author_email='anijackich@gmail.com',
    description='Python модуль для взаимодействия с образовательным порталом СДАМ ГИА',
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/anijackich/sdamgia-api',
    license='MIT',
    install_requires=['requests', 'beautifulsoup4', 'pyppeteer', 'grabzit'],
    packages = ['sdamgia'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
