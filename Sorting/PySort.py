#encoding=utf-8
__author__ = 'zym'

def binary_search(array,x,left,right):
    while(left<right):
        middle=(left+right)/2
        if x==array[middle]:
            return middle
        elif x>array[middle]:
            left=middle+1
        else:
            right=middle-1
    if x>array[middle]:
        return middle
    else:
        return middle-1

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

def merge_sort_recursive(array):
    length=len(array)
    if length==1:
        return array
    mid=length/2
    left_part=merge_sort_recursive(array[:mid])
    right_part=merge_sort_recursive(array[mid:])
    sorted_array=__merge_together(left_part,right_part)
    return sorted_array

def __merge_together(L,R):
    i=0
    j=0
    merged=[]
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            merged.append(L[i])
            i+=1
        else:
            merged.append(R[j])
            j+=1
    if i<len(L):
        merged.extend(L[i:])
    elif j<len(R):
        merged.extend(L[i:])
    return merged


def merge_sort(array_a):
    step=1
    length=len(array_a)
    array_b=list(array_a)
    while step<length:
        __merge_pass(array_a,array_b,step,length)
        step*=2
        __merge_pass(array_b,array_a,step,length)
        step*=2

def __merge_pass(array_from,array_to,step_len,length):
    i=0
    while i<length-2*step_len:
        __merge_into(array_from,array_to,i,i+step_len,i+2*step_len)
        i+=2*step_len
    #如果剩余元素够一组再进行一次归并
    if i+step_len<length:
        __merge_into(array_from,array_to,i,i+step_len,length)
    else:
    #作用1：如果元素不够一组那么直接把剩余元素copy到目标指针所指向的空间
    #作用2：一切元素都归并完成之后，把最终归并结果copy到A数组中。
        while i<length:
            array_to[i]=array_from[i]
            i+=1

def __merge_into(array_from,array_to,start_a,start_b,end):
    i=start_a
    j=start_b
    update_index=i
    while i<start_b and j<end:
        if array_from[i]<=array_from[j]:
            array_to[update_index]=array_from[i]
            i+=1
        else:
            array_to[update_index]=array_from[j]
            j+=1
        update_index+=1
    while i<start_b:
        array_to[update_index]=array_from[i]
        i+=1
        update_index+=1
    while j<end:
        array_to[update_index]=array_from[j]
        j+=1
        update_index+=1


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
