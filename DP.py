## DP를 이용한 피보나치 수열 구현
arr = [0]*100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if arr[x] != 0:
        return arr[x]
    arr[x] = fibo(x-1) + fibo(x-2)
    return arr[x]

print(fibo(99))


## DP 예제
n = int(input())

array = list(map(int, input().split()))

d = [0]*100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])