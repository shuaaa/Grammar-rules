#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:18:57 2020

@author: olamijojo
"""

class Stack(object):
    
    def __init__(self):
        
        """post: creates an empty LIFO stack"""
        self.items = []
        
        
    def push(self, item):
        
        """post: places x on top of the stack"""
        self.items.append(item)
        
    def pop(self):
        
        """pre: self.size() > 0
        post: removes and returns the top element of the stack"""
        return self.items.pop()
        
    def top(self):
        
        """pre: self.size() > 0
        post: reeturns the top element of the stack without removing it"""
        return self.items[-1]
    
    def size(self):
        
        """post: returns the number of elements in the stack"""
        return len(self.items)