# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:10:44 2022

@author: bryan
"""

matrix=[]

filas=4
columna=4
for i in range(filas):
    m=int(input("Ingrese los valores en las filas: "))
    matrix.append([m])
    for j in range(columna-1):
        n=int(input("Ingrese los valores en las columnas: "))
        matrix[i].append(n)