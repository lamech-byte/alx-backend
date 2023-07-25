#!/usr/bin/env python3
"""
100-lfu_cache.py
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}  # Dictionary to store the frequency of each key
        self.frequency_of_frequency = {}  # Dictionary to store
        self.min_frequency = 0

    def update_frequency(self, key):
        """ Update frequency of the key """
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        frequency = self.frequency[key]
        if frequency - 1 in self.frequency_of_frequency:
            self.frequency_of_frequency[frequency - 1].remove(key)

        if frequency not in self.frequency_of_frequency:
            self.frequency_of_frequency[frequency] = []

        self.frequency_of_frequency[frequency].append(key)

        if not self.frequency_of_frequency[self.min_frequency]:
            self.min_frequency += 1

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while not self.frequency_of_frequency[self.min_frequency]:
                    self.min_frequency += 1

                lfu_keys = self.frequency_of_frequency[self.min_frequency]

                if len(lfu_keys) == 1:
                    discarded_key = lfu_keys[0]
                else:
                    discarded_key = lfu_keys.pop(0)

                del self.cache_data[discarded_key]
                self.frequency.pop(discarded_key)

            self.cache_data[key] = item
            self.update_frequency(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None
