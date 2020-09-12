#!/bin/bash

# Install python dependencies
pip3 install -r $HOME/projects/acca-tracker/acca-tracker/requirements.txt

# Create bin folder
mkdir $HOME/bin
export PATH="$PATH:$HOME/bin"
export NEO4J_HOST="localhost:7687"

# Make cli executeable
chmod +x $HOME/projects/acca-tracker/acca-tracker/cli.py

# Symlink to python folder
ln -s $HOME/projects/acca-tracker/acca-tracker/cli.py $HOME/bin/accatracker
