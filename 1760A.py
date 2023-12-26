t = int(input())
while t:
    t -= 1
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr[1])
