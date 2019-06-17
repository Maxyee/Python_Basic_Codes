def print_swaps(arr):
    swaps = 0
    length = len(arr)
    for i in range(length - 1):
        for k in range(length - i - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                swaps += 1
    print(swaps)

N = int(input())
a = [int(x) for x in input().split()]
print_swaps(a)