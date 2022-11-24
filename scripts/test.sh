#!/usr/bin/env bash -ex

# Use `pytest-xdist --forked` to ensure modified `sys.path` for importing relative modules in examples
pytest --cov=typer_cloup_cli --cov=tests --cov-report=term-missing --cov-report=xml -o console_output_style=progress --forked --numprocesses=auto "$@"
