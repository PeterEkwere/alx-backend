#!/usr/bin/env python3
"""
    This Module contains the LRUCache thats a caching system
    Author: Peter Ekwere
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ FIFOCache system
    """

    def __init__(self):
        self.keys_count = []
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
                if key not in self.keys_count:
                    self.keys_count.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys_count[0])
                    print('DISCARD:', self.keys_count[0])
                    self.keys_count.pop(0)

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys_count.remove(key)
            self.keys_count.append(key)
        return value
