def recursion_sum(int_arr):
    if int_arr == []:
        return 0
    else:
        return int_arr.pop() + recursion_sum(int_arr)

def sumTriangle(arr):

    if len(arr) <= 1:
        print(arr)
        return

    # at every call, sum should happen.
    temp_arr = [0]*(len(arr)-1)
    i = 0
    while i < len(arr) - 1:
        temp_arr[i] = arr[i]+arr[i+1]
        i+=1
    
    sumTriangle(temp_arr)
    print(arr)

def consecutive_sum(arr,result):
    if len(arr) < 2:
        return
    consecutive_sum(arr[1:],result)
    result.append(arr[0]+arr[1])

    return
