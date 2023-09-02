from flask import Flask, request
import logging, os

LOG_FORMAT = "[%(asctime)s %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

DEBUG_MODE = os.environ.get('DEBUG', 'False') == 'True'

app = Flask(__name__)

@app.route('/')
def get_ip():
    user_ip = request.headers.get(request.remote_addr)
    return user_ip, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080, debug=DEBUG_MODE)
