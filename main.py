from flask import Flask
import redis
import os

REDIS_URL = os.getenv('REDIS_URL')

r = redis.Redis(host=REDIS_URL, port=6379, db=0)

app = Flask(__name__)

@app.get('/')
def index():
  return 'Translate API v1'

@app.get('/api/v1')
def apiv1():
  return 'Translate API v1'

@app.post('/api/v1/translate')
def translate():
  return { 'status': 'ok', 'message': None, 'data': None }
