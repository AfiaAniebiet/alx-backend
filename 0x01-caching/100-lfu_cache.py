#!/usr/bin/env python3

"""Create a class LFUCache that inherits
from BaseCaching and is a caching system
Must assign to the dictionary self.cache_data
the item value for the key key.If key or item
is None, this method should not do anything.If the
number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must
use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and
following by a new line"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

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
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.current_keys.append(self.current_keys.pop(
                self.current_keys.index(key)))
            return self.cache_data.get(key)
        return None
