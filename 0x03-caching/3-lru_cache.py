#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LIFO Cache"""

    def __init__(self):
        """Init the instance"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assing a key to a value"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.stack.pop(0)
            del self.cache_data[to_discard]
            print("DISCARD: {}".format(to_discard))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.move_to_last_in(key=key)

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        value = self.cache_data.get(key, None)
        if value is not None:
            self.move_to_last_in(key=key)
        return value

    def move_to_last_in(self, key):
        """Move an element to the init the list"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
