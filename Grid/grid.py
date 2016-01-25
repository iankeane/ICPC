# Unfinished

# Take in first two numbers as specified by the problem
n, m = raw_input().split(' ')
n = int(n)
m = int(m)

# Create an n x m array of zeros
arr = [[0 for x in range(m)] for x in range(n)] 

# Populate arrays with input from user
for x in range(0,n):
    tmp = list(raw_input())
    for y in range(0,m):
        arr[x][y] = int(tmp[y])

print(arr) # for testing
