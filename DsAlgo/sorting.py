#Bubble Sort
def bubble_sort(lt):
  
  temp = 0
  
  for i in range(0,len(lt)-1):
    for j in range(0,len(lt)-1-i):
      if lt[j] > lt[j+1]:
        temp = lt[j]
        lt[j] = lt[j+1]
        lt[j+1] = temp
        
  return lt

#Selection Sort with execution prints
def selection_sort(lt):
  
  for i in range(0,len(lt)-1):
    index = i
    print(lt)
    for j in range(i+1,len(lt)):
      print("i = {}, index = {} and j = {}, comparing {}  <  {}".format(i, index, j, lt[j], lt[index]))
      print("-----------")
      if lt[j] < lt[index]:
        index = j
        
    if index != i:
      swap(lt,index,i)
      print(lt)
      print("-------changed---------")
    
  return lt
  
#Insertion Sort  
def Insertion_sort(lt):
  
  for i in range(1,len(lt)):
    
    j = i
    
    while j > 0 and lt[j-1] > lt[j]:
      swap(lt,j,j-1)
      j = j-1
      
  return lt

def swap(ary, a, b):
  temp = ary[a]
  ary[a] = ary[b]
  ary[b] = temp
  return ary

#Quick Sort
def QuickSort(lt,low,high):
  
  if low >= high: return
  
  middle = partition(lt,low,high)
  QuickSort(lt,low,middle-1)
  QuickSort(lt,middle+1,high)
  
  return lt
    
def partition(lt,low,high):
  
  midindex = (low+high)//2
  swaps(lt,midindex,high)
  
  i=low
  
  for j in range(low,high,1):
    if lt[j] <= lt[high]:
      swaps(lt,i,j)
      i+=1
      
  swaps(lt,i,high)
      
  return i

def swaps(ary, a, b):
  temp = ary[a]
  ary[a] = ary[b]
  ary[b] = temp



lst = [14,3,5,12,-2,12]
#print(bubble_sort(lst)) 
#print(selection_sort(lst))
#print(Insertion_sort(lst))
print(QuickSort(lst,0,len(lst)-1))