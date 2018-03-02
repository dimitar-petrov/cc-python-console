# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ['click']
tests_require = ['pytest', 'pytest-cache', 'pytest-cov']


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

links = []
requires = []

requirements = pip.req.parse_requirements(
    'requirements.txt', session=pip.download.PipSession())

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, 'link', None): # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

setup(
    name="{{cookiecutter.repo_name}}",
    version='0.0.0',
    description="{{cookiecutter.description}}",
    long_description="\n\n".join([open("README.org").read()]),
    license='GPL 3.0',
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://{{cookiecutter.repo_name}}.readthedocs.org",
    packages=find_packages(),
    dependency_links=links,
    install_requires=requires,
    include_package_data=True,
    entry_points={'console_scripts': [
        '{{cookiecutter.console_app_name}} = {{cookiecutter.package_name}}.console:main']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GPL 3.0 License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest})
