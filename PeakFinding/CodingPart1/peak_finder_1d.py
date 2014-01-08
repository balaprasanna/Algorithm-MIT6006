def quick_find_1d_peak(array):
    """Finds a peak of a mountain range.

    The mountain range is a 1-dimensional array of values. A peak is
    defined as a location which is at least as high as the adjacent
    locations. Returns the index in the array of some peak.

    Keyword arguments:
    array -- an array containing the values

    returns the location x0 of the peak

    """

    ############## IMPLEMENT the O(log n) time algorithm here ############
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
    
    ##################################################################


def slow_find_1d_peak(array):
    best_x = 0
    best_h = array[0]
    for x in range(1, len(array)):
        h = array[x]
        if best_h < h:
            best_x = x
            best_h = h
    return best_x