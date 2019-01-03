import requests
import redis
from uuid import uuid4

r = redis.Redis(host="192.168.0.30")


def hit_server():
	"""
	function to get file from server
	"""
	path = str(uuid4())
	url = "http://10.0.0.1:8000/static/" + path
	response = requests.get(url)
	key_name = "client_side:" + str(response.elapsed.total_seconds()) + ":" + path
	print(key_name)
	r.set(key_name, 1)


for i in range(10000):
	hit_server()