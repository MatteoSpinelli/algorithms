""" Hash table are the fastest data strucutres for reading, inserting and deleting with an averege big O of O(1), and a worst of O(n) """
# in order to prevent the wors case, we have to carefully implement an hash function wich try the possible to avoid collision, wich create linked list with an O(n) of reading
# Hash maps are already implemented in language such as python with dictionaries, but here i'm going to try to implement one myself and track the performace

# load factor: num_of_item_in_has_table / num_of_slots
# if the load factor is greter than 1, your hash table is full
# rules of thumb:
# 1. resize the array when the load factor is greater tha 0.7
# 2. when resizing, double the size of the array



# feature:
# set_val(key, value)
# get(key), return none if not found
# delete(key)
# the print return a declarative log of the hash map
# the hash map has to resizing automatically

import copy
import random

class Hash_map:
    def __init__(self, initial_size = 10):
        self.size = initial_size
        self.hash_table = [[] for _ in range(self.size)]
        self.load_factor = self.load_factor_calc()

    def load_factor_calc(self):
        num_of_item = 0
        for item in self.hash_table:
            if item != []:
                for _ in item:
                    num_of_item += 1
        return num_of_item / self.size

    def resize(self):
        self.size = self.size * 2
        TEMP_HASH = copy.deepcopy(self.hash_table)
        self.hash_table = [[] for _ in range(self.size)]
        for item in TEMP_HASH:
            for el in item:
                key = el[0]
                value = el[1]
                self.insert_value(key, value)
        print(f"hash table has resize: {self.size / 2} => {self.size}")

    def insert_value(self, key, value):
        index = hash(key) % self.size
        for item in self.hash_table[index]:
            if item == (key, value):
                return
        self.hash_table[index].append((key, value))

    def set_val(self, key, value):
        self.insert_value(key, value)
        self.load_factor = self.load_factor_calc()
        if self.load_factor > 0.7:
            self.resize()

        print(self.hash_table)


hash_map = Hash_map(4)
for i in range(1000):
    hash_map.set_val(random.randint(0, 1000), random.randint(0, 1000))

            
    

