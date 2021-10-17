def bubbleSort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[5,7,2,58,64,1,23,0,78,21,13,46]
bubbleSort(arr)
print(arr)