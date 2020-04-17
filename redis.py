#!/bin/env python
import redis
import time
pool = redis.ConnectionPool(host="192.168.7.101", port=6379,password="")
r = redis.Redis(connection_pool=pool)
for i in range(100):
r.set("k%d" % i,"v%d" % i)
time.sleep(1)
data=r.get("k%d" % i)
print(data)