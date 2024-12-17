#!/bin/bash

echo "Starting Django server..."
cd backend
python3 manage.py runserver
BACKEND_PID=$!

sleep 5

echo "Starting React Native application..."
cd ../frontend
npm run ios &
FRONTEND_PID=$!

wait $BACKEND_PID
wait $FRONTEND_PID