rows,columns = list(map(int,input().split()))
counters=dict()
map=[ list(map(int,input().split()))[1::2] for _ in range(rows)]
print(mini,maxi, suma//(rows*columns))
