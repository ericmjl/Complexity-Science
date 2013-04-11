""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import string
import Generator


class LinearMap(object):
    """A simple implementation of a map using a list of tuples
    where each tuple is a key-value pair."""

    def __init__(self):
        self.items = []

    def add(self, k, v):
        """Adds a new item that maps from key (k) to value (v).
        Assumes that they keys are unique."""
        self.items.append((k, v))

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError


class BetterMap(object):
    """A faster implementation of a map using a list of LinearMaps
    and the built-in function hash() to determine which LinearMap
    to put each key into."""

    def __init__(self, n=100):
        """Appends (n) LinearMaps onto (self)."""
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        """Finds the right LinearMap for key (k)."""
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        """Adds a new item to the appropriate LinearMap for key (k)."""
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        """Finds the right LinearMap for key (k) and looks up (k) in it."""
        m = self.find_map(k)
        return m.get(k)
        
    def __len__(self):
        return len(self)



class HashMap(object):
    """An implementation of a hashtable using a BetterMap
    that grows so that the number of items never exceeds the number
    of LinearMaps.

    The amortized cost of add should be O(1) provided that the
    implementation of sum in resize is linear."""

    def __init__(self):
        """Starts with 2 LinearMaps and 0 items."""
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        return self.maps.get(k)

    def add(self, k, v):
        """Resize the map if necessary and adds the new item."""
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """Makes a new map, twice as big, and rehashes the items."""
        new_maps = BetterMap(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)

        self.maps = new_maps

import os

def etime():
    """See how much user and system time this process has used
    so far and return the sum."""

    user, sys, chuser, chsys, real = os.times()
    return user+sys

import string
import csv
import matplotlib.pyplot as pyplot

def store_data(map_type, data_size, time_elapsed):
    with open("data.csv", 'a') as csvfile:
        data = [map_type, data_size, time_elapsed]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)
        
        

def main(script):

    with open("data.csv", 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['map_type', 'data_size', 'time_elapsed'])
        
        
    values_to_test = [10**n for n in range(6)]
    print values_to_test
    
    for value in values_to_test:
        runs = 1
        while runs <= 5:
            s = list(xrange(value))
       
            """Characterize the time of Hashmap"""
            start = etime()
    
            m = HashMap()
        #     s = string.ascii_lowercase + string.ascii_uppercase

            for k, v in enumerate(s):
                m.add(k, v)

        #     for k in range(len(s)):
        #         print k, m.get(k)
        
            end = etime()
    
            elapsed = end - start
            print elapsed
            store_data('hashmap', len(s), elapsed)

            """Characterize the time of BetterMap"""
    
            start = etime()
    
            m = BetterMap()
    
            for k, v in enumerate(s):
                m.add(k, v)
    
            end = etime()
    
            elapsed = end - start
            print elapsed
    
            store_data('bettermap', len(s), elapsed)
    
            """Characterize the time of LinearMap"""
    
            start = etime()
    
            m = LinearMap()
    
            for k, v in enumerate(s):
                m.add(k, v)
    
            end = etime()
    
            elapsed = end - start
            print elapsed
            store_data('linearmap', len(s), elapsed)
            
            runs +=1 
    
    with open('data.csv', 'rU') as f:
        data = csv.DictReader(f)
        
        
        hashmap_xs = []
        hashmap_ys = []
        
        bettermap_xs = []
        bettermap_ys = []
        
        linearmap_xs = []
        linearmap_ys = []
        
        '''Get data out'''
        for row in data:
            if row['map_type'] == 'hashmap':
                hashmap_xs.append(row['time_elapsed'])
                hashmap_ys.append(row['data_size'])
            if row['map_type'] == 'bettermap':
                bettermap_xs.append(row['time_elapsed'])
                bettermap_ys.append(row['data_size'])
            if row['map_type'] == 'linearmap':
                linearmap_xs.append(row['time_elapsed'])
                linearmap_ys.append(row['data_size'])
                
        pyplot.plot(hashmap_xs, hashmap_ys)
        scale = 'log'
        pyplot.xscale(scale)
        pyplot.yscale(scale)
        pyplot.title('Hashmap Performance')
        pyplot.xlabel('n')
        pyplot.ylabel('run time (s)')
        pyplot.show()
        
        
        pyplot.plot(bettermap_xs, bettermap_ys)
        scale = 'log'
        pyplot.xscale(scale)
        pyplot.yscale(scale)
        pyplot.title('Bettermap Performance')
        pyplot.xlabel('n')
        pyplot.ylabel('run time (s)')
        pyplot.show()

        pyplot.plot(linearmap_xs, linearmap_ys)
        scale = 'log'
        pyplot.xscale(scale)
        pyplot.yscale(scale)
        pyplot.title('Linearmap Performance')
        pyplot.xlabel('n')
        pyplot.ylabel('run time (s)')
        pyplot.show()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
