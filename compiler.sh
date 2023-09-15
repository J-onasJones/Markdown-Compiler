#!/bin/bash
# This script compiles the source code for the project
# Usage: ./compiler.sh <input_file> <output_file> <mode>
# <mode> is optional
python src/markdown-compiler.py $1 $2 ${3:-}