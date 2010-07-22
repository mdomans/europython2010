CACHE_DICT = {}
import memcache
cache = memcache.Client(['localhost:11211'])

def cached(key):
    def func_wrapper(func):
        def arg_wrapper(*args, **kwargs):
            if not key in CACHE_DICT:
                value = func(*args, **kwargs)
                CACHE_DICT[key] = value
            return CACHE_DICT[key]
        return arg_wrapper
    return func_wrapper

def memcached(key):
    def func_wrapper(func):
        def arg_wrapper(*args, **kwargs):
            value = cache.get(str(key))
            if not value:
                value = func(*args, **kwargs)
                cache.set(str(key), value)
            return value
        return arg_wrapper
    return func_wrapper

def invalidate(key):
    try:
        del CACHE_DICT[key]
    except KeyError:
        print "someone tried to invalidate not present key: %s" %key

def mem_invalidate(key):
    cache.set(str(key), None)