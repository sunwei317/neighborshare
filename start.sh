#!/bin/bash

# Ensure script is run from the project root
# and venv exists at ./venv

# Screen session names
APP_SCREEN="neighborhoodshare"

# Activate the Python virtual environment command
ACTIVATE_CMD="source venv/bin/activate"

# Command to run Uvicorn
UVICORN_CMD="gunicorn -w 4 -b 127.0.0.1:8888 app:app"

echo "Starting server in screen: $APP_SCREEN"
screen -dmS $APP_SCREEN bash -c "$ACTIVATE_CMD && $UVICORN_CMD"

echo "All services started."
echo "Use 'screen -ls' to list sessions."
echo "Use 'screen -r <name>' to attach to a session."
