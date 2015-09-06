import heapq

def smallest(n,data):
    heapq.nsmallest(n, data)
    
def largest(n,data):
    heapq.nlargest(n, data)    