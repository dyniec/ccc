rows,columns = list(map(int,input().split()))
data = [ list(map(int,input().split()))[1::2] for _ in range(rows)]
dxs=[0,1,0,-1]
dys=[1,0,-1,0]
def get_neighbours(row, column):
    res=[]
    for dx,dy in zip(dxs,dys):
        x=row+dy
        y=column+dx
        if 0<= y < rows and 0<=x <columns:
            res.append(data[x][y])
    return res

def check_for_cell(data, column_idx, row_idx, rows, columns):
    if column_idx == 0 or row_idx == 0:
        return True
    if column_idx == columns-1 or row_idx == rows-1:
        return True

    neighbours = get_neighbours(row_idx,column_idx)
    is_border = [x != data[row_idx][column_idx] for x in neighbours]
    return any(is_border)
#for i in range(rows):
#    print (data[i])
counters=dict()
for i in range(rows):
    for j in range(columns):
        color = data[i][j]
#        if color == 2:
#            print(i,j,check_for_cell(data, j, i, rows,columns),get_neighbours(i,j))
        if color not in counters:
            counters[color]=0
        if check_for_cell(data, j, i, rows,columns):
            counters[color]+=1
maxi = max(counters.keys())
for i in range(maxi+1):
    res=0
    if i in counters:
        res=counters[i]
    print(res)
