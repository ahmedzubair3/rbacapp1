#!/bin/bash
set -e

source $HOME/.local/bin/env
mkdir -p data
exec uv run ./task3/script.py