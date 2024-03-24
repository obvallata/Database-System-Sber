import json
import redis
import time

file_path = 'products.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)

redis_client = redis.Redis(host='localhost', port=6379, db=0)

start = time.time()
p = redis_client.pipeline()
for pr in json_data:
    p.zadd(f'products_cost_sort', {pr['id']: pr['cost'] for pr in json_data})


p.execute()
print(time.time() - start)

# start = time.time()
# redis_client.get("products:3:amount")
# print(time.time() - start)
