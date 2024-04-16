import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_all_values(key:str):
    return r.hgetall(key)

def get_list_values(key: str):
    return r.lrange(key, 0, -1)

def get_specific_value(key:str, field: str):
    return r.hget(key, field)

def set_dict_value(key:str, value:dict):
    return r.hset(key, mapping=value)

def updated_specific_value(key: str, field: str, value):
    return r.hset(key, field, value)

def add_value_to_list(key: str, *args):
    return r.rpush(key, *args)

def remove_data_related_to_user(user_id: str):
    for key in r.scan_iter(f"*:{user_id}"):
        print(f"Deleting info for key: {key}")
        r.delete(key)

def clean_redis_database():
    database_cleaned = r.flushdb()
    if database_cleaned== True:
        print("base de datos limpiada")
    else:
        print("base de datos no limpiada")