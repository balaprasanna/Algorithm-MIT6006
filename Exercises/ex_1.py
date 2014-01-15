# -*- coding: utf-8 -*-
__author__ = 'zym'
import cProfile

"""
First problem:
Given a sorted integer array and an integer,
find the number of occurrences of this integer in the array.
If the integer does not appear in the array, return 0.
Time complexity requirement: log(N), where N is the size of the array.
"""
def solve_a(sorted_array,value):
    frequency=0
    left_index=find_left_boundry(sorted_array,value)
    #print left_index
    if left_index>=0:
        right_index=find_right_boundry(sorted_array,value)
        #print right_index
        frequency=right_index-left_index+1
    #print frequency
    return frequency

def find_left_boundry(sorted_array,value):
    left=0
    right=len(sorted_array)
    length=right
    while left<right:
        middle=(left+right)/2
        if sorted_array[middle]>value:
            right=middle
        elif sorted_array[middle]<value:
            if middle==length-1:
                return -1
            elif sorted_array[middle+1]<value:
                left=middle
            elif sorted_array[middle+1]>value:
                return -1
            elif sorted_array[middle+1]==value:
                return middle+1
        else:
            if middle==0 or sorted_array[middle-1]<value:
                return middle
            elif sorted_array[middle-1]==value:
                right=middle
    return -1

def find_right_boundry(sorted_array,value):
    left=0
    right=len(sorted_array)
    length=right
    while left<right:
        middle=(left+right)/2
        if sorted_array[middle]<value:
            left=middle
        elif sorted_array[middle]>value:
            if middle==0:
                return -1
            elif sorted_array[middle-1]>value:
                right=middle
            elif sorted_array[middle-1]<value:
                return -1
            else:
                return middle-1
        else:
            if middle==length-1 or sorted_array[middle+1]>value:
                return middle
            elif sorted_array[middle+1]==value:
                left=middle
    return -1


"""
Second problem:
Given an array A of characters and a character set S,
find the minimal window in A such that the window contains all characters in S.
Time complexity requirement: O(N), where N is the size of the array.
Note that a window may contain other characters not in S.
"""


def solve_b(array,char_set):
    array_length=len(array)
    char_count=len(char_set)
    char_dict=convert_to_dict(char_set)
    char_finded={}
    char_finded['min']=array_length
    window_width=array_length
    for i in range(array_length):
        if find_in_dict(array[i],char_dict):   #O(1)
            if find_in_dict(array[i],char_finded):
                update(char_finded)
            else:
                char_finded[array[i]]=i
            if len(char_finded)==char_count: #all char finded
                pass

def convert_to_dict(array):
    dict={}
    for elem in array:
        dict[elem]=True
    return dict

def find_in_dict(key,dict):
    try:
        return dict['key']==True
    except:
        return False

def update(char,index,dict):
    dict[char]=index
    pass


'''
Test your function now.
'''
def run(function_name,params):
    function_name(params)



if __name__=="__main__":
    cProfile.run("run()")
