# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:52:46 2020

@author: MONALIKA P
"""


class Product():
    def __init__(self,code,pname,man,price):
    
        self.code = code
        self.pname = pname
        self.man=man
        self.price = price
        
    def info(self):
        return "Code", self.code, "Product Name", self.pname, "Manufacturer", self.man, "Price", self.price
    
pList = []
pprice = []

p1 = Product(101,"JBL Head Phones","JBL",3000)
p2 = Product(301,"Vivo V6 Plus","Vivo",23000)
p3 = Product(601,"Asus Laptop","Asus",93000)
print(p1)
pList.append(p1)
pList.append(p2)
pList.append(p3)
print(pList)
total = 0 
pprice.append(p1.price)
pprice.append(p2.price)
pprice.append(p3.price)
print(pprice)
for p in pList:
    print(p.info())
    total =total + p.price
  
print("Total" ,total)
print("Maximum price of the products is " ,max(pprice))
print("Minimum price of the products is " ,min(pprice))
