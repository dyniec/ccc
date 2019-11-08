k = int(input())
panel_price = []
panel_country = []
for _ in range(k):
    a, b = list(map( int, input().split()))
    panel_country.append(a)
    panel_price.append(b)


rows,columns = list(map(int,input().split()))
map_country = []
map_altitude = []
countries_num=0
for i in range(rows):
    row = list(map(int,input().split()))
    map_country.append(row[1::2])
    map_altitude.append(row[::2])
    countries_num=max(countries_num,max(row[1::2])+1)
    
dxs=[0,1,0,-1]
dys=[1,0,-1,0]
class Country:
    def __init__(self,color):
        self.color=color
        self.row=0
        self.column=0
        self.count=0
        self.inner=[]
        self.edges=[]
def get_neighbours(row, column):
    res=[]
    for dx,dy in zip(dxs,dys):
        x=row+dy
        y=column+dx
        if 0<= y < rows and 0<=x <columns:
            res.append(map_country[x][y])
    return res

def check_if_border(column_idx, row_idx):
    if column_idx == 0 or row_idx == 0:
        return True
    if column_idx == columns-1 or row_idx == rows-1:
        return True

    neighbours = get_neighbours(row_idx,column_idx)
    is_border = [x != map_country[row_idx][column_idx] for x in neighbours]
    return any(is_border)

capitals =[Country(color) for color in range(countries_num)]
for i in range(rows):
    for j in range(columns):
        color = map_country[i][j]
        capitals[color].row+=i
        capitals[color].column+=j
        capitals[color].count+=1
        if check_if_border(j,i):
            # krawedz
            capitals[color].edges.append((i,j))
        else:
            # w srodku
            capitals[color].inner.append((i,j))
def squared_euclid(a,b):
     (x1,y1)=a
     (x2,y2)=b
     return (x1-x2)**2 + (y1-y2)**2

     
for country in capitals:
    row=country.row//country.count
    column=country.column//country.count
    average=(row,column)
    if map_country[row][column]==country.color:
        if not check_if_border(column,row):
            print(column,row)
            continue
    candidate=country.inner[0]
    smallest_dist=squared_euclid(average,candidate)
    for field in country.inner[1:]:
        dist=squared_euclid(field,average)
        if dist < smallest_dist:
            candidate=field
            smallest_dist=dist
    (row,column)=candidate
    print(column, row)
        
    
