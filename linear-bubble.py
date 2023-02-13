# linear search

arr = [10,20,30,40,50]
find = int(input("Enter the number want to search: \n "))



def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("Found at index " , arr) 
        else: 
            print("Not found")
linear_search(arr,find)
