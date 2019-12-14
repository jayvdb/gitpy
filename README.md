
# gitpy

Python Interface to GitHub developer's API

---

[![Build Status](https://travis-ci.org/babygame0ver/gitpy.svg?branch=master&style=flat-square)](https://travis-ci.org/babygame0ver/gitpy)
[![Code Climate](https://codeclimate.com/github/babygame0ver/gitpy.png?style=flat-square)](https://codeclimate.com/github/babygame0ver/gitpy)
[![codecov](https://codecov.io/gh/babygame0ver/gitpy/branch/master/graph/badge.svg)](https://codecov.io/gh/babygame0ver/gitpy)

---

## Dependencies

[![Python](https://img.shields.io/badge/python-3.7.4-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-374/)
[![Requests](https://img.shields.io/badge/requests-2.22.0-blue.svg?style=flat-square)](https://pypi.python.org/pypi/requests/)
[![Coverage](https://img.shields.io/badge/Coverage-4.5.4-blue.svg?style=flat-square)](https://pypi.org/project/coverage/)
[![codecov](https://img.shields.io/badge/codecov-4.5.4-blue.svg?style=flat-square)](https://pypi.org/project/codecov/)

---

## Installation Guide

```

# git clone https://github.com/babygame0ver/gitpy.git && cd gitpy
# pip install -r requirements.txt
# python3 setup.py install

```

## Run test suite

```
# python3 -m unittest discover
# coverage run -m unittest discover

```

---

A command line package purely written in Python3 consumes GitHub developer's API and provides all the functionalities in one place using Python Function.

* Core : Deals with authentication with GitHub API using Authentication token.

* Repository : Deals with information & actions related to both public & private Repositories.

---

## Documentation

[gitpy Docs](documentation.rst)
