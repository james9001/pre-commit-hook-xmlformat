"""Fake setup for pre-commit hook."""

from setuptools import setup

setup(
    name='pre-commit-hook-xmlformat',
    description='A pre-commit hook to format XML files',
    url='https://github.com/james9001/pre-commit-hook-xmlformat',
    version='1.0.0',

    install_requires=[],

    scripts=[
        'pre_commit_hooks/xml_format',
    ],

    # explicitly declare packages so setuptools does not attempt auto discovery
    # taken from https://github.com/pypa/setuptools/issues/3197
    packages=[],
)