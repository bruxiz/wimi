from flask import Flask, request
import logging, os

LOG_FORMAT = "[%(asctime)s %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

DEBUG_MODE = os.environ.get('DEBUG', 'False') == 'True'

app = Flask(__name__)

@app.route('/')
def get_ip():

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        user_ip = x_forwarded_for.split(',')[0]
    else:
        user_ip = request.remote_addr
    return user_ip + " X-Forwarded-For header not found", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=DEBUG_MODE)
