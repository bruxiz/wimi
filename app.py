from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_ip():

    client_ips = request.headers.get('X-Forwarded-For', request.remote_addr)
    original_client_ip = client_ips.split(',')[0].strip()

    return f'Hello, your IP is: {original_client_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
