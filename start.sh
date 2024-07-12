#!/bin/bash

echo "Starting Fast API server..."
cd backend
python3 main.py
BACKEND_PID=$!

sleep 2

echo "Starting React Native application..."
cd ../frontend
npm run ios &
FRONTEND_PID=$!

wait $BACKEND_PID
wait $FRONTEND_PID