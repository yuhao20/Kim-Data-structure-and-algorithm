def heap_create(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]<arr[l]:
        largest=l  #后期统一交换

    if r<n and arr[largest]<arr[r]:
        largest=r

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]

        heap_create(arr,n,largest)

def heap_sort(arr):
    n=len(arr)

    for i in range(n,-1,-1):          #构造堆
        heap_create(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]   #交换最大值arr[0]
        heap_create(arr,i,0)          #此处不用循环了
                                      #原因:整个框架都没变除了最大值和最后一个值
                                    
