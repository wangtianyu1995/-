##字符串匹配问题：其主要功能给定两个字符串T和f（字串），长度分别为n和m，判断f是否在T中出现，如果出现则返回出现的位置。
# 给定两个字符串T和f（字串），长度分别为n和m，判断f是否在T中出现，如果出现则返回出现的位置。如：有一个字符串
# "BBC ABCDAB ABCDABCDABDE"，我想知道，里面是否包含另一个字符串"ABCDABD"？

# 朴素字符串匹配算法：遍历T的每一个位置，然后从该位置开始和f进行匹配，但是这种方法的复杂度是O(nm)。
# 这种算法没有利用匹配过的信息，对于字串来说每次都从头开始比较，而对于主串来说，经常需要重复比较之前已经检测过的字符，
# 因而速度很慢。模式匹配是一个常见的应用问题，用的广了，就有人想法去优化了。Rabin-Karp算法、有限自动机等等，前仆后继，
# 最终出现了KMP(Knuth-Morris-Pratt)算法。
# kmp算法被称为“看毛片”算法安静，是一个效率非常高的字符串匹配算法。

# kmp算法通过一个O(m)的预处理来构建一个字串f的前缀数组（即计算字符串f每一个位置的字符串的前缀和后缀公共部分的最大长度，
# 不包括字符串本身，否则最大长度始终是字符串本身），接下来的匹配过程会不断地使用到该前缀数组（而且对于主串T只需遍历一次），
# 使匹配的复杂度降为O(n+m)。

def getnext(a,next):  
    al = len(a)  
    next[0] = -1  
    k = -1  
    j = 0  
    while j < al-1:  
        if k == -1 or a[j] == a[k]:  
            j += 1  
            k += 1  
            next[j] = k  
        else:  
            k = next[k]  
  
def KmpSearch(a,b):  
    i = j = 0  
    al = len(a)  
    bl = len(b)  
    while i < al and j < bl:  
        if j == -1 or a[i] == b[j]:  
            i += 1  
            j += 1  
        else:  
            j = next[j]  
    if j == bl:  
        return i-j  
    else:  
        return -1  
  
a = 'ABABCABDABBGAFDSBVSABDABBfgdgd'  
b = 'ABDABB'  
next = [0]*len(b)  
getnext(b,next)  
t = KmpSearch(a,b)  
# print(next)  
print(t)

