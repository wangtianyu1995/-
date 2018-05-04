##进行二分查找算法前必须保证要查找的序列时有序的，这里假设是升序列表
def binary_search(find, list1) :
  low = 0
  high = len(list1)
  while low <= high :
    mid = (low + high) // 2
    if list1[mid] == find :
      return mid
    #左半边
    elif list1[mid] > find :
      high = mid -1
    #右半边
    else :
      low = mid + 1
  #未找到返回-1
  return -1

list1 = [1,2,3,7,8,9,10,15]
print("被查找数的下标：",binary_search(7,list1))
