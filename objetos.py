# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:29:26 2018

@author: cquei
"""

class Retangulo:
    def area(self):
        return self.a * self.l
    
    
    def membros_retangulo(r):
        r.a = 0
        r.l = 0
        
    r1 = Retangulo()
    membros_retangulo(r1)
    r1.l = 10
    r1.a = 5
    
    print( r1.area() )
    print( r1.area() )