#!/bin/bash

# Set environment variables
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

echo "Setup complete. Activate the virtual environment with 'source venv/bin/activate'"
