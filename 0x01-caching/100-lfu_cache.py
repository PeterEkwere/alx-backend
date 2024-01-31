#!/usr/bin/env python3
"""
    This Module contains the LFUCache thats a caching system
    Author: Peter Ekwere
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ MRUCache system
    """

    def __init__(self):
        self.keys_count = {}
        super().__init__()

    def put(self, key, item):
        """ updates cache_data with the key and item

        Args:
            key (_type_): cache key
            item (_type_): cache value
        """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    k = min(self.keys_count, key=self.keys_count.get)
                    self.cache_data.pop(k)
                    print('DISCARD:', k)
                    self.keys_count.pop(k)
                if key not in self.keys_count:
                    self.keys_count[key] = 0

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys[key] += 1
        return value
