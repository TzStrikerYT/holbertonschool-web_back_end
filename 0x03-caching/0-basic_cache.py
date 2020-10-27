#!usr/bin/python3
""" 0-basic_cache.py - basic cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache"""

    def put(self, key, item):
        """ put() - Put elements in a dic
        Arguments:
        key: key of dictionary
        item: value of dictionary
        Returns: updated dictionary self.cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get() - another .get
        Arguments:
        key: key of dictionary
        Returns dictionary value pertaining to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
