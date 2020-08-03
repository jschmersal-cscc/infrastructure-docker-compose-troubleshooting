import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='db', port=6379)

def hits():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def basic():
    count = hits()
    return 'this application has been viewed {} times.\n'.format(count)
