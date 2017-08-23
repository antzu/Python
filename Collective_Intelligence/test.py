#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 07:49:55 2017

@author: andres
"""

from recommendations import critics
from recommendations import sim_distance
from recommendations import sim_pearson




for p in critics:
    print(p)
    


#Testing simdistance
sim_distance(critics,'Lisa Rose','Gene Seymour')
sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')


