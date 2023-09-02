from flask import Flask, request
import pprint

app = Flask(__name__)

def print_request_info(req):
    print("=== Headers ===")
    pprint.pprint(dict(req.headers))
    print("\n=== Method ===")
    print(req.method)
    print("\n=== Full Path ===")
    print(req.full_path)
    print("\n=== Remote Address ===")
    print(req.remote_addr)
    print("\n=== Data ===")
    print(req.data)
    print("\n=== Form ===")
    pprint.pprint(req.form)
    print("\n=== Args ===")
    pprint.pprint(req.args)
    print("\n=== JSON ===")
    pprint.pprint(req.json)
    print("===================")

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print_request_info(request)

    client_ips = request.headers.get('X-Forwarded-For', request.remote_addr)
    original_client_ip = client_ips.split(',')[0].strip()

    return f'Hello, your IP is: {original_client_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
