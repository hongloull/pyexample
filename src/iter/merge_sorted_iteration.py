import heapq

a=[1,3,4]
b=[2,5,8]
for i in heapq.merge(a,b):
    print(i)
# 1
# 2
# 3
# 4
# 5
# 8
