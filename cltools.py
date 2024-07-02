# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 02:46:39 2024

@author: Vinicius
"""



def elbow(x,y):
    slopes=[]
    var=[]
    for i in range(1,len(x)):
        slopes.append([x[i],(y[i]-y[i-1])/(x[i]-x[i-1])])
        if i>=2:
            var.append([x[i-1],slopes[i-2][1]/slopes[i-1][1]])
    return var

def create_rank(X):
    rk=[]
    X_sort = sorted(X, key=lambda x: x[1], reverse=True)
    for i in range(len(X_sort)):
        rk.append([X_sort[i][0],len(X_sort)-i])
    return rk 

def combine_ranks(rk1, rk2, values=False):
    final_rk=[]
    if values:
        col = 2
    else:
        col = 1
    for item1 in rk1:
        for item2 in rk2:
            if item1[0] == item2[0]:
                final_rk.append([item1[0],item1[col]+item2[col]])
    return sorted(final_rk, key=lambda x : (x[1],x[0]), reverse=True)