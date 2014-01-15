#encoding=utf-8
__author__ = 'zym'

def insertion_sort(array):
    '''
    find the right position for array[i]
    insert to the right position and move others to the right
    '''
    length=len(array)
    for i in range(1,length):
        j=i
        value=array[i]
        while j>0 and value<array[j-1]:
            array[j]=array[j-1]
            j-=1
        array[j]=value
    return array

def merge_sort():
    pass

def bubble_sort():
    pass

def select_sort():
    pass


def quick_sort():
    pass


def heap_sort():
    pass

def radix_sort():
    pass
