#encode=utf-8
__author__ = 'zym'
from utils_2d import *


def find_cross_row_max(matrix, x, y0, y1):
    """add by zym to find max value in the row and column"""
    best_y = y0
    best_h = matrix[x][best_y]
    for y in range(y0 + 1, y1+1):
        h = matrix[x][y]
        if best_h < h:
            best_y = y
            best_h = h
    return best_y, best_h

def find_cross_column_max(matrix, x0, x1, y):
    """add by zym to find max value in the row and column"""
    best_x = x0
    best_h = matrix[best_x][y]
    for x in range(x0 + 1, x1+1):
        h = matrix[x][y]
        if best_h < h:
            best_x = x
            best_h = h
    return best_x, best_h



def quick_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implement O(n) solution given in lecture.
    """
    nrows=len(matrix)
    ncols=len(matrix[0])
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
            elif (crossmax_y==y0 and y0>0):
                """if the max value hit the boundary inside the space"""
                if row_max[1]<matrix[mid_x][crossmax_y-1]:
                    #TODO: cross the boundary to it's left neighbour's square.
                    x1=mid_x
                    y1=y0
                    y0=y0-(mid_y-y0)
                else:
                    return(crossmax_x,crossmax_y)
            elif (crossmax_y==y1 and y1<ncols-1):
                if row_max[1]<matrix[mid_x][crossmax_y+1]:
                    #TODO: cross the boundary to it's left neighbour's square.
                    x1=mid_x
                    y0=y1
                    y1=y1+(y1-mid_y)
                else:
                    return(crossmax_x,crossmax_y)
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
            elif (crossmax_x==x0 and x0>0):
                """if the max value hit the up or down boundary inside the space"""
                if col_max[1]<matrix[crossmax_x-1][mid_y]:
                    #TODO: cross the boundary to it's upper neighbour's square.
                    x1=x0
                    x0=x0-(x0-mid_x)
                    y0=mid_y
                else:
                    return(crossmax_x,crossmax_y)
            elif (crossmax_x==x1 and x1<nrows-1):
                if col_max[1]<matrix[crossmax_x+1][mid_y]:
                    #TODO: cross the boundary to it's lower neighbour's square.
                    x0=x1
                    x1=x1+(x1-mid_x)
                    y0=mid_y
                else:
                    return(crossmax_x,crossmax_y)
            else:
                return crossmax_x, crossmax_y



(n, matrix) = read_input("9_big_spiral.txt")
(x, y) = quick_find_2d_peak(matrix, 0, n - 1, 0, n - 1)
print (x, y)
print matrix[x][y]