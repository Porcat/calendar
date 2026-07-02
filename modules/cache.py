# =========================
# 简单内存缓存（避免重复计算）
# =========================

_lunar_cache = {}
_event_cache = {}


def get_cache(cache, key):
    return cache.get(key)


def set_cache(cache, key, value):
    cache[key] = value
    return value