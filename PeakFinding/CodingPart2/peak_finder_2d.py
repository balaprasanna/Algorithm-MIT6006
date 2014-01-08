import sys

############### Auxiliary functions #####################

def find_cross_row_max(matrix, x, y0, y1):
    """add by zym to find max value in the row and column"""
    best_y = y0
    best_h = matrix[x][best_y]
    for y in range(y0 + 1, y1 + 1):
        h = matrix[x][y]
        if best_h < h:
            best_y = y
            best_h = h
    return best_y, best_h

def find_cross_column_max(matrix, x0, x1, y):
    """add by zym to find max value in the row and column"""
    best_x = x0
    best_h = matrix[best_x][y]
    for x in range(x0 + 1, x1 + 1):
        h = matrix[x][y]
        if best_h < h:
            best_x = x
            best_h = h
    return best_x, best_h


def find_column_global_max(matrix, x, y0, y1):
    """ Finds global maximum of column x between rows y0 and y1 (inclusive). """
    best_y = y0
    best_h = matrix[x][best_y]
    for y in range(y0+1, y1+1):
        h = matrix[x][y]
        if best_h < h:
            best_y = y
            best_h = h
    return (best_y, best_h)

def find_row_global_max(matrix, x0, x1, y):
    """ Finds global maximum of row y between columns x0 and x1 (inclusive). """
    best_x = x0
    best_h = matrix[best_x][y]
    for x in range(x0+1, x1+1):
        h = matrix[x][y]
        if best_h < h:
            best_x = x
            best_h = h
    return (best_x, best_h)

def find_global_max(matrix, x0, x1, y0, y1):
    """ Finds global maximum of sub-matrix between columns x0 and x1 and rows y0 and y1 (inclusive). """
    best_x = x0
    best_y = y0
    best_h = matrix[best_x][best_y]
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            h = matrix[x][y]
            if(best_h < h):
                best_x = x
                best_y = y
                best_h = h
    return (best_x, best_y, best_h)

############################################################


####################### Algorithms Implementation #########################

"""Find a peak of a mountain range.

The mountain range is a 2-dimensional matrix of integers values,
indexed by closed intervals [x0,x1] and [y0,y1].

A peak is defined as a location which is at least as high as the adjacent
locations (two locations are adjacent if they share a common edge).

Keyword arguments:
matrix -- a matrix of altitudes
x0 -- an integer which is the leftmost index of the range
x1 -- an integer which is the rightmost index of the range
y0 -- an integer which is the bottom-most index of the range
y1 -- an integer which is the topmost index of the range

Return value: a pair of coordinates (x, y) of any local maximum location

"""

def quick_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implement O(n) solution given in lecture.
    """

    ########### WRITE YOUR IMPLEMENTATION HERE ############

    while x0 < x1 and y0 < y1:
        mid_x = (x0 + x1) / 2
        mid_y = (y0 + y1) / 2
        row_max = find_cross_row_max(matrix, mid_x, y0, y1)
        col_max = find_cross_column_max(matrix, x0, x1, mid_y)
        if row_max[0]==mid_y and col_max[0]==mid_x:
            return mid_x, mid_y
        if row_max[1] >= col_max[1]:
            crossmax_x = mid_x
            crossmax_y = row_max[0]
            if crossmax_y < mid_y and row_max[1] < matrix[mid_x - 1][crossmax_y]:
                #TODO: find peak in the top-left sub-square
                x1 = mid_x
                y1 = mid_y
            elif crossmax_y < mid_y and row_max[1] < matrix[mid_x + 1][crossmax_y]:
                #TODO: find peak in the bottom-left sub-square
                x0 = mid_x
                y1 = mid_y
            elif crossmax_y > mid_y and row_max[1] < matrix[mid_x - 1][crossmax_y]:
                #TODO: find peak in the top-right sub-square
                x1 = mid_x
                y0 = mid_y
            elif crossmax_y > mid_y and row_max[1] < matrix[mid_x + 1][crossmax_y]:
                #TODO: find peak in the bottom-right sub-square
                x0 = mid_x
                y0 = mid_y
            else:
                return (crossmax_x, crossmax_y)
        else:
            crossmax_x = col_max[0]
            crossmax_y = mid_y
            if crossmax_x < mid_x and col_max[1] < matrix[crossmax_x][mid_y - 1]:
                #TODO: find peak in the top-left sub-square
                x1 = mid_x
                y1 = mid_y
            elif crossmax_x > mid_x and col_max[1] < matrix[crossmax_x][mid_y - 1]:
                #TODO: find peak in the bottom-left sub-square
                x0 = mid_x
                y1 = mid_y
            elif crossmax_x < mid_x and col_max[1] < matrix[crossmax_x][mid_y + 1]:
                #TODO: find peak in the top-right sub-square
                x1 = mid_x
                y0 = mid_y
            elif crossmax_x > mid_x and col_max[1] < matrix[crossmax_x][mid_y + 1]:
                #TODO: find peak in the bottom-right sub-square
                x0 = mid_x
                y0 = mid_y
            else:
                return crossmax_x, crossmax_y


    #######################################################


def medium_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implements O(n log(n)) solution given in lecture.
    """
    
    while x0 < x1: 

        mid_x = (x0+x1)/2 # If the width of the range is even,
                          # this picks the cell slightly to the left of the middle
 
        mid_col_glob_max = find_column_global_max(matrix, mid_x, y0, y1)
        right_col_glob_max = find_column_global_max(matrix, mid_x + 1, y0, y1)

        if right_col_glob_max[1] > mid_col_glob_max[1]:
            x0 = mid_x + 1 # choose the right half
        else:
            x1 = mid_x # choose the left half
             
    max_y_and_value = find_column_global_max(matrix, x0, y0, y1)
    return (x0, max_y_and_value[0])


def slow_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implements O(n^2) solution given in lecture.
    """
    result = find_global_max(matrix, x0, x1, y0, y1)
    return (result[0], result[1])
##########################################################################