#!/bin/bash
set -e

# Start core services
sudo service apache2 start
sudo service rabbitmq-server start
sudo service postgresql start


source $HOME/.local/bin/env
mkdir -p ./data
mkdir -p ./logs

# Start monitoring server as background daemon
echo "🚀 Starting monitor_services.py as HTTP service on port 5001..."
nohup uv run monitor_services.py > ./logs/monitor.log 2>&1 &

# # Start the main Flask API server in foreground (port 5000)
# echo "🚀 Starting Flask API server (app.py)..."
exec uv run app.py
# sleep infinity 