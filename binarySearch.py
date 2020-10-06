def binarySearch(what,arr):

    li = 0

    ls = len(arr)-1

    while li<=ls:

          middle = (li+ls)/2

          if(what == arr[middle]):

             return middle

          elif what > arr[middle]:

             li = middle + 1

          else:

             ls = middle - 1    

    return False 
