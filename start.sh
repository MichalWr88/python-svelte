#!/bin/bash

export FLASK_APP=app.py
export FLASK_ENV=development
flask run &

cd ./frontend
npm run dev

