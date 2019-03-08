# Redis, stands for REmote DIctionary Server, is a BSD-licensed, in-memory data structure store
# Redis is an in-memory key-value pair database typically classified as a NoSQL database.
# Redis is commonly used for caching,
#   transient data storage and as a holding area for data during analysis in Python applications.
# Redis developers can leverage data structures like strings, hashes, lists, sets, and sorted sets using
#   commands similar to the collection operations in most programming languages.
# Redis has replication capabilities, a server-side scripting language (Lua), transactions,
#   and different modes of disk persistence.
# Reference: https://opensource.com/article/18/4/how-build-hello-redis-with-python

# Steps:
# Import the Redis library
import redis

# Define connection parameters
redis_host = "localhost"
redis_port = 6379
redis_password = ""

# Instantiate the Redis connection object
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
# The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
# using the default encoding utf-8.  This is client specific.

# step 4: Set the hello message in Redis
r.set("hello", "Hello Redis!!!")  # Setting key:value pair

# step 5: Retrieve the hello message from Redis
msg = r.get("hello")  # Retrieving value using key
print(msg)
