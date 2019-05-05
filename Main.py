inp = input().split(" ")
inp = [int(x) for x in inp]
arr = []
arr = input().split(" ")
arr = [int(x) for x in arr]
arr = arr[::-1]
k = len(arr)
for i in arr:
    if inp[1]==i:
        print(k)
        break
    k=k-1