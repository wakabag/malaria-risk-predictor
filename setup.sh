#!/bin/bash

# Install system dependencies (if any)
if [ -f packages.txt ]; then
    sudo apt-get update
    sudo apt-get install -y $(cat packages.txt)
fi

# Install Python dependencies
pip install -r requirements.txt
