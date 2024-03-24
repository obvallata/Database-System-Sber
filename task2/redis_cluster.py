from redis.cluster import RedisCluster as Redis
import json
import time

file_path = 'products.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)

redis_client =Redis(host='localhost', port=7010)

# start = time.time()
# p = redis_client.pipeline()
# for pr in json_data:
#     for field in ('product_name', 'cost', 'amount'):
#         p.set(f'products:{pr["id"]}:{field}', pr[field])
#
#
# p.execute()
# print(time.time() - start)

# start = time.time()
# redis_client.hset('gen', mapping=json_data)
# print(time.time() - start)

start = time.time()
redis_client.get("products:3:amount")
print(time.time() - start)
