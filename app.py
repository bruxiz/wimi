from flask import Flask, request

app = Flask(__name__)

def print_request_info(req):
    print("=== Headers ===")
    print(dict(req.headers))
    print("\n=== Method ===")
    print(req.method)
    print("\n=== Full Path ===")
    print(req.full_path)
    print("\n=== Remote Address ===")
    print(req.remote_addr)
    print("\n=== Data ===")
    print(req.data)
    print("\n=== Form ===")
    print(req.form)
    print("\n=== Args ===")
    print(req.args)

    content_type = req.headers.get('Content-Type')
    if content_type == 'application/json':
        print("\n=== JSON ===")
        print(req.json)
    else:
        print("\n=== JSON ===")
        print("Did not attempt to load JSON data because the request Content-Type was not 'application/json'.")
    
    print("===================")

@app.route('/')
def hello_world():
    print_request_info(request)

    client_ips = request.headers.get('X-Forwarded-For', request.remote_addr)
    original_client_ip = client_ips.split(',')[0].strip()

    return f'Hello, your IP is: {original_client_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
