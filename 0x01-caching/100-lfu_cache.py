#!/usr/bin/env python3
"""
100-lfu_cache.py
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = defaultdict(int)
        self.min_frequency = 0
        self.order = []

    def update_frequency(self, key):
        """ Update frequency of the key """
        self.frequency[key] += 1
        if self.frequency[key] > self.min_frequency:
            self.min_frequency = self.frequency[key]

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [
                    k for k, v in self.frequency.items()
                    if v == self.min_frequency
                ]
                for k in self.order[:]:
                    if k in lfu_keys:
                        self.order.remove(k)
                        del self.cache_data[k]
                        del self.frequency[k]
                        print("DISCARD: {}".format(k))

                self.min_frequency += 1

            self.cache_data[key] = item
            self.update_frequency(key)
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None
