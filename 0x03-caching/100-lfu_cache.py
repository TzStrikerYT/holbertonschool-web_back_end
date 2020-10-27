#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LIFO Cache"""

    def __init__(self):
        """Init the instance"""
        super().__init__()
        self.stack = []
        self.stack_count = {}

    def put(self, key, item):
        """Assing a key to a value."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.stack_count.get(key, None)

        if item_count is not None:
            self.stack_count[key] += 1
        else:
            self.stack_count[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.stack.pop(0)
            del self.stack_count[to_discard]
            del self.cache_data[to_discard]
            print("DISCARD: {}".format(to_discard))

        if key not in self.stack:
            self.stack.insert(0, key)

        self.move_to_right(item=key)

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        value = self.cache_data.get(key, None)
        if value is not None:
            self.stack_count[key] += 1
            self.move_to_right(item=key)

        return value

    def move_to_right(self, item):
        """Add 1 for all elements less the key"""
        length = len(self.stack)

        idx = self.stack.index(item)
        item_count = self.stack_count[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.stack[i + 1]
                nxt_count = self.stack_count[nxt]

                if nxt_count > item_count:
                    break

        self.stack.insert(i + 1, item)
        self.stack.remove(item)
