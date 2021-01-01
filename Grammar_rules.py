#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:16:11 2020

@author: olamijojo
"""
from Grammar import *

def test():
    gram = Grammar()
    gram.addRule("S-> NP VP")       # Rule 1
    gram.addRule("NP -> ART N")     # Rule 2
    gram.addRule("NP -> PN")        # Rule 3
    gram.addRule("VP -> V NP")      # Rule 4
    gram.addRule("V -> chased")     # Rule 5
    gram.addRule("ART -> the")      # Rule 6
    gram.addRule("N -> dog")        # Rule 7
    gram.addRule("N -> cat")        # Rule 8
    gram.addRule("PN -> Emily")     # Rule 9
    gram.addRule("N -> Pussy")
    gram.addRule("IRV -> got")      # IRV - irregular verb
    gram.addRule("ADJ -> wet")      # ADJ - adjective
    gram.addRule("ADJP -> IRV ADJ") # ADJP - adjectival phrase
    gram.addRule("S -> NP ADJP")      
    
    #print(gram.generate("ART"))
    #print(gram.generate("N"))
    #print(gram.generate("VP"))
    print(gram.generate("S"))
        
test()


 