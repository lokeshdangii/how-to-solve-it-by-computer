# Algorithm for finding the maximum in a set by comparing each number with all other number 
def maxiMum(arr):
    ele_max = arr[0]
    maximum = arr[0]

    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[j]>= arr[i]:
                ele_max = arr[j]
            if ele_max >= maximum:
                maximum = ele_max
    # print(ele_max)   
    print("The maximum number in an array : ",maximum)
    return maximum


arr1= [12,12,65,13,11,64,24,875,34,2334,12,33,1,6,9,232,23]
maxiMum(arr1)
