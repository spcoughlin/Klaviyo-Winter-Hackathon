#!/bin/bash
set -e

echo "Starting BirdieDeals backend..."
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT