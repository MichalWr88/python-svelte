#!/bin/bash

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
  echo "requirements.txt not found!"
  exit 1
fi

# Create a virtual environment in the 'venv' directory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Print the path to the virtual environment's Python interpreter
echo "Virtual environment created and dependencies installed."
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "Python interpreter path: $(which python)"