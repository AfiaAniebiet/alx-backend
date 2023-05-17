#!/usr/bin/env python3
"""Create a class MRUCache that inherits from
BaseCaching and is a caching system. If key or
item is None, this method should not do anything.
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            else:
                self.current_keys.append(self.current_keys.pop(
                    self.current_keys.index(key)))
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(-2)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.current_keys.append(self.current_keys.pop(
                self.current_keys.index(key)))
            return self.cache_data.get(key)
        return None