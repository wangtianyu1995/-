##https://www.cnblogs.com/tuhooo/p/7092288.html哈西原理
##https://blog.csdn.net/waltonhuang/article/details/52325416解决哈希冲突
##python数据结构https://www.yiibai.com/python/py_data_structure/python_hash_table.html

# ##开发地址法
# def changeKey(key,m,di):
#     key01=(key+di)%m
#     return key01    

# a = input("Please entry the numbers:\n").split()
# print(a,type(a))
# m=len(a)
# print(m)
# dict01={}
# for  i in  a:
#     key=int(i)%m
#     print(i)
#     print(key)
#     if "%s"%key in dict01:
#         newKey=changeKey(key,m,1)
#         while "%s"%key in dict01:
#             newKey=changeKey(newKey,m,1)
#             dict01["s"%newKey]=int(i)
#     else:
#         dict01["key"]=int(i)

# print(dict01)


###链表法

def chainHash(InputList): 
    res = {}
    for line in InputList:
        if line.split()[0] not in res:
            temp = []        #因为在拉链法中，键值包含多个对象，因此需要新建一个列表，把键值保存在这个列表中
            temp.append(line.split()[1])
            res["%s" % line.split()[0]] = temp
        else:
            res["%s" % line.split()[0]].append(line.split()[1])
    return res

InputList=["key01 val01"]
print(chainHash(InputList))

    
