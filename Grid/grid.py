n, m = raw_input().split(' ')
n = int(n)
m = int(m)
arr = [[0 for x in range(m)] for x in range(n)] 

for x in range(0,n):
    tmp = list(raw_input())
    for y in range(0,m):
        arr[x][y] = int(tmp[y])

print(arr)
