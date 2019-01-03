from flask import Flask, request, send_from_directory
import redis

r = redis.Redis(host="192.168.0.30")
app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_file(path):
	client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	key_name = "server_side:" + client_ip + ":" + path
	print(key_name)
	r.set(key_name, '1')
	return send_from_directory('static', 'golang.png')


# if __name__ == '__main__':
# 	app.run()
