#encode=utf-8
__author__ = 'zym'

from utils_1d import *
def quick_find_1d_peak(array):
    left=0
    right=len(array)-1
    x0=(left+right)/2
    while True:

        if x0>0 and array[x0]<array[x0-1]:
            right=x0
            x0=(left+right)/2
        elif x0<len(array)-1 and array[x0]<array[x0+1]:
            left=x0
            x0=(left+right)/2+1
        else:
            return x0


array =(11,5,2,1,0)
peakPos=quick_find_1d_peak(array)
print array[peakPos],peakPos