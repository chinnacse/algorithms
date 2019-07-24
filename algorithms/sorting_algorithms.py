from sorting_algorithms_helpers import merge_sort, quick_sort, heapify
if __name__ == '__main__':
    pass
else:
    def insertionSort(array):
        for i in range(1,len(array)):
            key = array[i]

            j = i-1
            while j>=0 and key < array[j]:
                array[j+1] = array[j]
                j-=1
            array[j+1]=key
        return array


    def selectionSort( array):
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                if array[min_index]>array[j]:
                    min_index=j
            array[i], array[min_index] = array[min_index], array[i]
        return array


    def bubbleSort(array):
        for i in range(0, len(array)):
            for j in range(0,len(array)-i-1):
                if array[j]> array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j] 
        return array


    def mergeSort(array):
        start = 0 
        end = len(array)
        return merge_sort(array, start, end)

    def quickSort(array):
        first_index = 0
        last_index = len(array)-1
        return quick_sort( array, first_index, last_index)


    def heapSort(array): 
        n = len(array) 
        for i in range(n, -1, -1): 
            heapify(array, n, i) 
    
        for i in range(n-1, 0, -1): 
            array[i], array[0] = array[0], array[i] 
            heapify(array, i, 0)

        return array 

