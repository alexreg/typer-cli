#!/usr/bin/env bash -ex

mypy typer_cloup_cli
black typer_cloup_cli tests --check
isort typer_cloup_cli tests --check-only
