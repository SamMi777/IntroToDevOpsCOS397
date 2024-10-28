# IntroToDevOpsCOS397

## Overview
In this repository there are implementations of Bubble Sort, Quick Sort, and Insertion Sort algorithms written in Python, all located in the `basic_sort_UNIQUE_SUFFIX\int_sort.py` directory.

There are also detailed tests that ensure the success and validity of each of our sorting algorithms, these are located in the `test\test_basic_sort.py` directory.

There is a defined `.pre-commit-config.yml` file that limits maximum file size, runs the flake8 and black linters, and detects the aws credentials' private keys.

The GitHub workflow is defined in the `.github\workflows\main.yml` directory. Here you will find the primary implementation of DevOps CI/CD which automates the linting process using both the flake8 and black linters. It then follows by automating each of our tests to ensure our sorting algorithms are functional. Finally, if the tests pass, the workflow will build the package and push its artifact to GitHub Actions, detailing the status of all attempted jobs in the workflow.

## Prerequisites
**Python 3.9 or 3.10** are the only currently supported Python versions that must be installed.
**Git** must be configured for version control, code and branch management.

## Workflow Badge
![Build Status](https://github.com/SamMi777/IntroToDevOpsCOS397/actions/workflows/main.yml/badge.svg)
