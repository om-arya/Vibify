#!/bin/bash

echo "Starting React Native application..."
cd frontend
npm run ios &
FRONTEND_PID=$!

sleep 3

echo "Starting Django server..."
source backend/bin/activate
cd ../backend/vibify
python3 manage.py runserver
BACKEND_PID=$!

wait $FRONTEND_PID
wait $BACKEND_PID