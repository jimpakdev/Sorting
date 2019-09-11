# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    aIndex = bIndex = mIndex = 0

    while aIndex != len(arrA) and bIndex != len(arrB):
        if arrA[aIndex] < arrB[bIndex]:
            merged_arr[mIndex] = (arrA[aIndex])
            aIndex += 1
            mIndex += 1
        else:
            merged_arr[mIndex] = (arrB[bIndex])
            bIndex += 1
            mIndex += 1

    if aIndex < len(arrA):
        merged_arr = merged_arr[ 0 : mIndex ] + arrA[ aIndex : ]
    
    elif bIndex < len(arrB):
        merged_arr = merged_arr[ 0 : mIndex ] + arrB[ bIndex : ]

    # merged_arr = arrA + arrB
    # merged_arr.sort()
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) < 2:
        return arr

    else: 
        arrL = merge_sort( arr[ : int(len(arr)/2) ] )
        arrR = merge_sort( arr[ int(len(arr)/2) : ] )

        arr = merge( arrL, arrR )

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
