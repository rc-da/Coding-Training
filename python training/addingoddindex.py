arr = [1,2,3,4,5,6,7,8,9,10]
odd_index_add = 0

for i in range(1,len(arr),2):
    odd_index_add += arr[i]
print(odd_index_add)