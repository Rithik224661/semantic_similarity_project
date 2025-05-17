#!/bin/bash

# Create necessary directories
mkdir -p ~/.streamlit/

# Set up Streamlit config (if needed)
echo "\n[server]\nheadless = true\nport = $PORT\nenableCORS = false\n" > ~/.streamlit/config.toml

# Set environment variables
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Install Python dependencies if not already installed
if [ ! -d "venv" ]; then
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source venv/bin/activate
fi
