#!/usr/bin/env bash -ex

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place typer_cloup_cli tests --exclude=__init__.py
black typer_cloup_cli tests
isort typer_cloup_cli tests
