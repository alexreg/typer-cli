#!/usr/bin/env bash -ex

mypy typer_cli
black typer_cli tests --check
isort typer_cli tests --check-only
