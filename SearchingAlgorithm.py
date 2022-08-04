import math

# ============================================================================
def linearSearchForMultiplePresence(arr, sizeofarray, valuetosearch):
    """A linear searching algorithm which finds if a given value exists in an array.
If it does, at which indexes and how many times.
Takes (an array, size/length of the array, and a value to search for) as parameter.
Call the funtion to get indexes only, print the function to get the number of times
the value appeared."""
    c=-1
    for i in range(0, sizeofarray):
        if (arr[i] == valuetosearch):
            # return i
            print(f"The given element {valuetosearch} is present at index {i}")
            c+=1
        # else:
        #     return -1
    if(c == -1):
        print("Element is not present in array")
    return f"The number is found {c+1} times"
# linearSearchForMultiplePresence.__doc__ = '''A linear searching algorithm which finds if a given value exists in an array.
# If it does, at which indexes and how many times.
# Takes (an array, size/length of the array, and a value to search for) as parameter.
# Call the funtion to get indexes only, print the function to get the number of times
# the value appeared. '''

# .........................................................................................
def linearSearchForSinglePresence(arr, sizeofarray, valuetosearch):
    """\nA linear searching algorithm which finds if a given value exists in an array. 
If it does, at which index.
Takes (an array, size/length of the array, and a value to search for) as parameter."""
    c=-1
    for i in range(0, sizeofarray):
        if (arr[i] == valuetosearch):
            c=i
            break
            
    if(c == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", c)


# =========================================================================
def binarySearchRecursive (arr, left, right, valuetosearch):
    """\nA binary searching algorithm(Recursive) which finds if a given value exists in an sorted array. 
If it does, at which index.
Takes (an array, 0(zero), size/length of the array-1, and a value to search for) as parameter."""
  
    # Check base case
    if right >= left:
  
        mid = left + (right - left) // 2
  
        # If element is present at the middle itself
        if arr[mid] == valuetosearch:
            # return mid
            print("Element is present at index", mid)
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > valuetosearch:
            return binarySearchRecursive(arr, left, mid-1, valuetosearch)
  
        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearchRecursive(arr, mid + 1, right, valuetosearch)
  
    else:
        # Element is not present in the array
        print("Element is not present in the array")


# ============================Exponential Search=========================================================
def exponentialSearch(arr, n, x):
    """\nAn exponential searching algorithm(Recursive) which finds if a given value exists in an sorted array. 
If it does, at which index.
Takes (an array, size/length of the array, and a value to search for) as parameter.
Later calls on binary search.
Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite.
It works better than Binary Search for bounded arrays, and also when the element to be searched is closer to the first element."""
  
    # IF x is present at first
    # location itself
    if arr[0] == x:
        return 0
         
    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
     
    # Call binary search for the found range
    return binarySearchRecursive( arr, i // 2,
                         min(i, n-1), x)
# .........................................................................................
def binarySearchIterative(arr, left, right, valuetosearch):
    """\nA binary searching algorithm(Iterative) which finds if a given value exists in an sorted array. 
If it does, at which index.
Takes (an array, 0(zero), size/length of the array-1, and a value to search for) as parameter."""
  

    c=0
    while left <= right:
  
        mid = left + (right - left) // 2
          
        # Check if x is present at mid
        if arr[mid] == valuetosearch:
            # return mid
            c+=1
            print("Element is present at index", mid)
            break
            
  
        # If x is greater, ignore left half
        elif arr[mid] < valuetosearch:
            left = mid + 1
  
        # If x is smaller, ignore right half
        else:
            right = mid - 1
      
    # If we reach here, then the element
    # was not present
    if c==0:
        print("Element is not present in the array")


# ===================================================================================
def jumpSearch( arr , lengthofarray , valuetosearch ):
    """\nA jump searching algorithm, which finds if a given value exists in an sorted array. 
If it does, at which index.
Takes (an array, size/length of the array, and a value to search for) as parameter."""

    try:
                # Finding block size to be jumped
        step = int(math.sqrt(lengthofarray))

        # Finding the block where element is
        # present (if it is present)
        prev = 0
        while arr[int(min(step, lengthofarray)-1)] < valuetosearch:
            prev = step
            step += int(math.sqrt(lengthofarray))
            if prev >= lengthofarray:
                print("Element is not found")
                break
            
        # Doing a linear search for x in
        # block beginning with prev.
        while arr[int(prev)] < valuetosearch:
            prev += 1

            # If we reached next block or end
            # of array, element is not present.
            if prev == int(min(step, lengthofarray)):
                print("Element is not found")
                break
            
        # If element is found
        if arr[int(prev)] == valuetosearch:
            print(f"Number {valuetosearch} is present at {prev}")
            

        
        return -1

    except Exception as e:
        print(f"We encountered an Error: {e}")

# =======================================================================================
def interpolationSearch(arr, lo, hi, x):
    """\nAn interpolation searching algorithm, which finds if a given value exists in an sorted array. 
If it does, at which index.
Takes (an array, 0(zero), size/length of the array-1, and a value to search for) as parameter."""
 
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    count=0
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 
        # Condition of target found
        if arr[pos] == x:
            count+=1
            print("Element is present at index ", pos)
 
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    if count==0:
        print("Element is not present in array")

# ======================KMP ALGORITHM=======================================
def kmpTextSearch(pat, txt):
    """\nA KMP searching algorithm, which finds if a given value(pattern/string/character) exists in an sorted array. 
If it does, at which index.
Takes (a pattern and a string) as parameter."""
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                
            else:
                lps[i] = 0
                i += 1


# Driver Code
if __name__=="__main__":
# ======LINEAR SEARCH=======================================================
    arr = [2, 3, 4, 10, 40, 54, 12, 10, 65, 10, 45, 78, 100, 65, 10]
    x = 10
    n = len(arr)
    
    # Function call
    result = linearSearchForMultiplePresence(arr, n, x)
    result = linearSearchForSinglePresence(arr, n, x)
    # if(result == -1):
    #     print("Element is not present in array")
    # else:
    #     print("Element is present at index", result)


# ===============BINARY SEARCH=====================================================
    arr2 = [ 2, 3, 4, 10, 40]
    x2 = 10
  
    
    # Function call
    result2 = binarySearchRecursive(arr2, 0, len(arr2)-1, x)
    result2 = binarySearchIterative(arr2, 0, len(arr2)-1, x2)

    # ======================JUMP SEARCH===================================================================
    arr3 = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
        34, 55, 89, 144, 233, 377, 610, 700 ]
    x3 = 701
    n2 = len(arr)
    
    # Find the index of 'x' using Jump Search
    index = jumpSearch(arr3, n2, x3)
    
    # ====================INTERPOLATION SEARCH==============================================
    arr4 = [10, 12, 13, 16, 18, 19, 20,
           21, 22, 23, 24, 33, 35, 42, 47]
    n3 = len(arr)
    
    # Element to be searched
    x4 = 18
    index2 = interpolationSearch(arr4, 0, n3 - 1, x4)
    
# =========================KMP TEXT SEARCH====================================================
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmpTextSearch(pat, txt)

# ====================================================================================
    arr5 = [ 2, 3, 4, 10, 40]
    x5 = 10
    n4=len(arr2)

    expo=exponentialSearch(arr5, n4, x5)


# ============EXAMPLE==================================================
# &&&&&&&&&&&&EXAMPLE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




# import Project1.SearchingAlgorithm as search

# arr = [2, 3, 4, 10, 40, 54, 12, 10, 65, 10, 45, 78, 100, 65, 10]
# x = 10
# n = len(arr)
# myDict={
#     "math": "Is important",
#     "code": "Should be done regularly",
#     "marks": [1,2,3],
#     1: 10,
#     "value": 10

# }
# m='code'

# print(search.linearSearchForMultiplePresence(arr,n,x))
# search.linearSearchForMultiplePresence(list(myDict.keys()),len(myDict),m)
# search.linearSearchForMultiplePresence(arr,n,x)
# search.linearSearchForSinglePresence(arr,n,x)
# x = dir(search)
# print(search.linearSearchForMultiplePresence.__doc__)
# print(search.binarySearchIterative.__doc__)
# print(search.interpolationSearch.__doc__)