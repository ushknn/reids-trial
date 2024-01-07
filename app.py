from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')    
    view_count = redis.get('hits').decode('utf8')
    return f'Hello World! I have been seen {view_count} times.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)