# Python program for implementation of devide and concuer
def MaxIndex(arr, l, r): 
    if l == r: return l
    else:
      temp1 = MaxIndex(arr, l, ((l+r)//2)) 
      temp2 = MaxIndex(arr, 1 + ((l+r)//2), r)
      if(arr[temp1] >= arr[temp2]): return temp1
      else: return temp2
        
  
# Driver Code 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr) 
ten = MaxIndex(arr, 0, len(arr)-1) 
print ("Largest in given array is", ten)
