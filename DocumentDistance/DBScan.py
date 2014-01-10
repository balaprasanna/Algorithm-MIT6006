# -*- coding: utf-8 -*-
__author__ = 'zym'
import DocumentDistance
def get_neighbors(index,data,eps):
    """
    neighbors=[id1,id2,...]
    """
    neighbors=[]
    data_count=len(data)
    for i in range(index+1,data_count):
        distance=DocumentDistance.get_distance(data[index],data[i])
    pass

def dbscan(eps,minpts,data):
    docs=data[0]
    births=data[1]
    ids=data[2]
    data_count=len(docs)
    for i in range(data_count-1):
        neighbors=get_neighbors(i,docs,eps)
