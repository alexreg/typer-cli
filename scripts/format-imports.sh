#!/usr/bin/env bash -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --recursive  --force-single-line-imports --thirdparty typer_cloup_cli --apply typer_cloup_cli tests

./scripts/format.sh
