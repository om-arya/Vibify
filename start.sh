#!/bin/bash

echo "Starting React Native application..."
cd ../frontend
npm run ios &
FRONTEND_PID=$!

sleep 5

echo "Starting Django server..."
cd backend
python3.10 manage.py runserver
BACKEND_PID=$!

wait $FRONTEND_PID
wait $BACKEND_PID