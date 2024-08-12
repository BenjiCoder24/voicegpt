#!/bin/sh

pip3 install Flask flask-cors python-dotenv
pip3 install gunicorn

#pip3 install fastapi
#pip3 install uvicorn[standard]
pip3 install openai
pip3 install gtts
#pip3 install pydub
pip3 install python-multipart

python3 app.py

# uvicorn app:app --host=0.0.0.0 --port=3000

# For development use (simple logging, etc):
# python3 server.py
# For production use: 
# gunicorn server:app -w 1 --log-file -