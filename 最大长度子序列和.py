#http://www.jb51.net/article/129824.htm

##o(n*n)的解法
##最简单粗暴的方式，双层循环，用一个maxsum标识最大连续子序列和。然后每次判断更新。没有太多可以说的，直接上代码
# list1=[2,4,1,-4,5,2,3,-2,4]
# def maxSUM(list1):
#     maxsum=list1[0]
#     for i in range(len(list1)):
#         maxtemp=0
#         for i in range(len(list1)):
#                 maxtemp+=list1[j]
#                 if maxtemp>maxsum:
#                     maxsum=maxtemp   
#     return maxsum

##o(n)的解法
##假设数组为a[i],最大连续的子序列和必须是在位置0-(n-1)之间的某个位置结束。那么，当循环遍历到第i个位置时，
# 如果其前面的连续子序列和小于等于0，
# 那么以位置i结尾的最大连续子序列和就是第i个位置的值即a[i]。如果其前面的连续子序列和大
# 于0，则以位置i结尾的最大连续子序列和为b[i] = max{ b[i-1]+a[i]，a[i]}，其中b[i]就是指最大连续子序列的和。

# def maxSUM(list1):
#     maxsum=0
#     maxtmp=0
#     for i in range(len(list1)):
#         if maxtmp<=0:
#             maxtmp=list1[i]
#         else maxsum>0:
#             maxtmp+=list1[i]

#         if maxtmp>maxsum:
#             maxsum=maxtmp

#         return maxsum

    
