#https://blog.csdn.net/u013719780/article/details/49201143
#http://python.jobbole.com/82270/

# #insert sort o(n*n) 稳定
#
# def insert_sort(list_argv):
#     count=len(list_argv)
#     for i in range(1,count):
#         j=i-1
#         key=list1[i]
#         while j>=0:
#             if key<list1[j]:
#                 list1[j+1]=list1[j]
#                 list1[j]=key
#                 print(list1)
#             j=j-1
#     return list1
#
# insert_sort(list1)


#shell sort 平均o(nlogn) 标准o(n的m次方)

# def shell_sort(list_argv):
#     count=len(list_argv)
#     step=2
#     group=int(count/step)
#     while group>0:
#         for i in range(group):
#             j=i+group
#             while j<count:
#                 key=list_argv[j]
#                 k=j-group
#                 while k>=0:
#                     if list_argv[k]>key:
#                         list_argv[k+group]=list_argv[k]
#                         list_argv[k]=key
#                     k=k-group
#                 j=j+group
#         group=group/step
#     return list_argv

#select sort
# def select_sort(list_argv):
#     count=len(list_argv)
#     for i in range(0,count):
#         min =i
#         for j in range(i+1,count):
#             if list_argv[min]>list_argv[j]:
#                 min=j
#                 list_argv[min],list_argv[i]=list_argv[i],list_argv[min]
#     return list_argv

#quick sort

# def quick_sort(lists, left, right):
#     if left >= right:
#             return lists
#     key = lists[left]
#     low = left
#     high = right
#     while left < right:
#         while left < right and lists[right] >= key:
#             right -= 1
#         lists[left] = lists[right]
#         while left < right and lists[left] <= key:
#             left += 1
#         lists[right] = lists[left]
#     lists[right] = key
#     quick_sort(lists, low, left - 1)
#     quick_sort(lists, left + 1, high)
#     return lists

# #heap_sort
# def adjust_heap(list1,i,size):
#     lchild=2*i+1
#     rchild=2*i+2
#     max=i
#     if i<size//2
#         if lchild<size and list1[lchild]>list1[max]:
#             max=lchild
#         if rchild<size and list1[rchild]>list1[max]:
#             max=rchild
#         if max=i:
#             list1[max],list1[i]=list1[i],list1[max]
#             adjust_heap(list1,max,size)


# def build_heap(list1,size):
#     for i in range(0,(size//2))[::-1]:
#         adjust_heap(list1,i,size)

# def heap_sort():
#     list1=[43,23,67,45,89,54,67,90]
#     size=len(list1)
#     build_heap(list1,size)
    
# heap_sort()


#radix_sort
import math

list1=[43,23,67,45,89,54,67,90]

def radix_sort(list1,radix=10):
   k=int(math.ceil(math.log(max(list1),radix)) )
   bucket=[[] for i in range(radix_sort)]
   for i in range(1,k+1):
       for j in list1:
           list1[j//(radix**(i-1))%(radix**i)].append(j)
           del list1[:]
           for z in bucket:
               list1+=z
               del z[:]
    return list1

radix_sort(list1)




