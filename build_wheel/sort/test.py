import time
import sort
import sort_code
import numpy as np

a = np.random.rand(1000).tolist()# [5, 3, 10, 20, 1, 0, 9]
def bubbleSort():
    t = time.time()
    ret = sort.bubbleSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.bubbleSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

def selectionSort():
    t = time.time()
    ret = sort.selectionSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.selectionSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

def insertionSort():
    t = time.time()
    ret = sort.insertionSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.insertionSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

def shellSort():
    t = time.time()
    ret = sort.shellSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.shellSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

def mergeSort():
    t = time.time()
    ret = sort.mergeSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.selectionSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

def quickSort():
    t = time.time()
    ret = sort.quickSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)

    t = time.time()
    ret = sort_code.quickSort(a)
    print("time: ", time.time()-t)
    # print("ret: ", ret)





if __name__ == "__main__":
    import fire
    fire.Fire()