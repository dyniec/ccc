rows,columns = list(map(int,input().split()))
suma = 0
mini=10**10
maxi = 0
for i in range(rows):
    row= list(map(int,input().split()))
    mini=min(min(row),mini)
    maxi=max(max(row),maxi)
    suma += sum(row)
print(mini,maxi, suma//(rows*columns))
