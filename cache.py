cache = set()

def exists(key):

    return key in cache


def save(key):

    cache.add(key)