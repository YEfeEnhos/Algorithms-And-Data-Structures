def heappush(heap, x):
    heap.append(x)
    if len(heap)>1:
        for i in range(1,len(heap)):
            if i//2>0 and heap[i]<heap[i//2]:
                heap[i],heap[i//2]=heap[i//2],heap[i]
            elif i//2>0 and heap[i] == heap[i//2] and heap[i]<heap[(i//2)+1]:
                heap[i],heap[(i//2)+1]=heap[(i//2)+1],heap[i]
                
    return heap

def heappop(heap):
   heap.pop(1)
   if heap[1]>heap[2]:
       heap[1],heap[2]=heap[2],heap[1]
   
   

def hepify(li):
    for i in range(len(li)):
        heappush(heap, li[i])
    return heap

def soart(heap):
    out=[]
    heap.remove(heap[0])
    for i in range(len(heap)):
        out.append(min(heap))
        heap.remove(min(heap))
    return out


li=[1,6,8,4,10,7,3]


heap=["None"]

