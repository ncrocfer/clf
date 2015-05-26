#!/usr/bin/env python

from setuptools import setup

entry_points = {
    'console_scripts': [
        'clf = clf:run',
    ]
}
requirements = open('requirements.txt').read()
readme = open('README.rst').read()

setup(
    name="clf",
    version="0.5.4",
    url='http://github.com/ncrocfer/clf',
    author='Nicolas Crocfer',
    author_email='ncrocfer@gmail.com',
    description="Command line tool to search snippets on Commandlinefu.com",
    long_description=readme,
    packages=['clf'],
    include_package_data=True,
    install_requires=requirements,
    entry_points=entry_points,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
