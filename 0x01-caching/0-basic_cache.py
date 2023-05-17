#!/usr/bin/env python3

"""A class BasicCache that inherits from BaseCaching
and is a caching system. You must use self.cache_data
- dictionary from the parent class BaseCaching. This
caching system doesn’t have limit"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Dict caching system """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
