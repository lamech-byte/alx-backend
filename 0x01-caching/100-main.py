#!/usr/bin/env python3
"""
100-main.py
"""
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()

print("Current cache:")
my_cache.print_cache()

my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")

print("Current cache:")
my_cache.print_cache()

print(my_cache.get("B"))
print(my_cache.get("A"))

my_cache.put("E", "Battery")
print("Current cache:")
my_cache.print_cache()

my_cache.put("C", "Street")
print("Current cache:")
my_cache.print_cache()

print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
print(my_cache.get("E"))

my_cache.put("F", "Mission")
my_cache.put("G", "San Francisco")
print("Current cache:")
my_cache.print_cache()

my_cache.put("H", "H")
my_cache.put("I", "I")
print("Current cache:")
my_cache.print_cache()

my_cache.put("J", "J")
my_cache.put("K", "K")
my_cache.put("L", "L")
print("Current cache:")
my_cache.print_cache()

my_cache.put("M", "M")
print("Current cache:")
my_cache.print_cache()
