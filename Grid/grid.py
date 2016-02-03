# Unfinished
lastcount = 100

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

def search(arr, i, j, count):
    count += 1
    global lastcount, m, n
    k = arr[i][j]
    print(count)
    # Check ending case
    if(i == m-1 and j == n-1):
        print("TRUE")
        if(lastcount > count):
            lastcount = count
            count = 0
            return lastcount - 1
        else:
            count = 0
            return lastcount - 1
    # Check if value is zero (dead end)
    if(arr[i][j] == 0):
        count = 0
        return
    # Check if count is too big
    if(count > m*n):
        return
    # Up
    try:
        search(arr,i-k,j, count)
    except IndexError:
        pass
    # Down
    try:
        search(arr,i+k,j, count)
    except IndexError:
        pass
    # Left
    try:
        search(arr,i,j-k, count)
    except IndexError:
        pass
    # Right
    try:
        search(arr,i,j+k, count)
    except IndexError:
        pass
    return lastcount - 1

print(search(arr,0,0,0))
