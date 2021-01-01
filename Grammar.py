#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:21:49 2020

@author: olamijojo
"""
import random
from Stack import Stack
#ffg code is a context free Gramma class CFG- class

class Grammar(object):
    
    def __init__(self):
        self.rules = []
        self.nonterms = []    # tracks the non-terminals in the grammar 
         
    
    def addRule(self, rule):
        # split the rule at the arrow
        
        lhs, rhs = rule.split("->")
        
        # extract the non-terminal, ignoring spaces
        nt = lhs.strip()
        
        # split the rhs into a list of symbols and reverse it
        symbols = rhs.spli()
        symbols.reverse()
        
        # pair the non-terminalwith the symbol sequence and store it 
        self.rules.append((nt,symbols))
        
        # update the non-terminal list
        if nt not in self.nonterms:
            self.nonterms.append(nt)
            
            
        def generate(self, start):
            s = Stack()
            s.push(start)
            output = []
            while s.size() > 0:
                top = s.pop()
                if self.isTerminal(top):
                    
                    # does'nt expand, it's part of the output
                    output.append(top)
                else:
                    
                    # choose one expansion from all that might be used 
                    cands = self.getExpansions(top)
                    expansion = random.choice(cands)
                    # push the chosen expansioin onto the stack
                    for symbol in expansion:
                        s.push(symbol)
            return " ".join(output)
    
    def isTerminal(self, term):
        return term not in self.nonterms
    
    def getExpansions(self, nt):
        expansions = []
        
        for (nt1, expansion) in self.rules:
            if nt1 == nt:         # this rule matches
                copy = list(expansion)
                expansions.append(copy)
        return expansions
    
    
    