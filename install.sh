#!/bin/bash

# Install python dependencies
pip3 install -r $HOME/projects/acca-tracker/acca-tracker/requirements.txt

# Create bin folder
mkdir $HOME/bin
echo 'export PATH="$PATH:$HOME/bin"' >> ~/.bashrc
echo 'export NEO4J_HOST="localhost:7687"' >> ~/.bashrc
source ~/.bashrc

# Make cli executeable
chmod +x $HOME/projects/acca-tracker/acca-tracker/cli.py

# Symlink to python folder
ln -s $HOME/projects/acca-tracker/acca-tracker/cli.py $HOME/bin/accatracker
