from fractions import Fraction as F
hours_num = int(input())
rays = [list(map(int,input().split())) for _ in range(hours_num)]

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
def country_dist(a,b):
    ret=int(math.sqrt(squared_euclid( (a.row,a.column),(b.row,b.column))))
    return ret

     
for country in capitals:
    row=country.row//country.count
    column=country.column//country.count
    average=(row,column)
    if map_country[row][column]==country.color:
        if not check_if_border(column,row):
            country.row=row
            country.column=column
            continue
    candidate=country.inner[0]
    smallest_dist=squared_euclid(average,candidate)
    for field in country.inner[1:]:
        dist=squared_euclid(field,average)
        if dist < smallest_dist:
            candidate=field
            smallest_dist=dist
    (row,column)=candidate
    country.row=row
    country.column=column
        
    
for country in capitals:
    for ray in rays:
        for field in country.inner:
            (x,y)=field
            if 0<=x or x>=rows-1:
                continue
            if 0<=y or y>=columns-1:
                continue
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    new_field=(x+dx,y+dy)
                    if new_field not in country.inner:
                        continue
                    if map_altitude[x+dx][y+dy]!=map_altitude[x,y]:
                        continue
                    
                    
                 

def straight(o,d):
    (ox,oy)=o
    (dx,dy)=d
    result = []
    horizontal = 1 if dx>0 else -1
    vertical = 1 if dy>0 else -1
    if dx==0: horizontal=0
    if dy==0: vertical=0
    while 0<=ox<columns and 0<=oy<rows:
        result.append((ox,oy))
        ox+=horizontal
        oy+=vertical
    return result
    
def one_test(o,d):
    (ox,oy)=o
    (dx,dy)=d
    horizontal = 1 if dx>0 else -1
    vertical = 1 if dy>0 else -1
    next_vertical = F(1,2)*horizontal+ox
    next_horizontal = F(1,2)*vertical + oy
    if dx==0 or dy==0:
        return straight(o,d)
    dominant_horizontal= abs(dx)>= abs(dy)

    x=F(ox)
    y=F(oy)
    solution=[]
    while 0<=ox<columns and 0<=oy<rows:
        time_to_horizontal= (next_horizontal-y)/dy
        time_to_vertical = (next_vertical-x)/dx
        time=min(time_to_horizontal,time_to_vertical)
        """print(time1,time2,time)
        print(float(x),float(y) )
        print(ox,oy)
        print("next", next_vertical, next_horizontal)"""
        if time_to_horizontal==time_to_vertical:
            solution.append((ox,oy))
            if dominant_horizontal:
                solution.append((ox+horizontal,oy))
                solution.append((ox,oy+vertical))
            else:
                solution.append((ox,oy+vertical))
                solution.append((ox+horizontal,oy))
            x+=dx*time
            y+=dy*time
            ox+=horizontal
            oy+=vertical
            next_vertical+=horizontal
            next_horizontal+=vertical
        else:
            solution.append((ox,oy))
            x+=dx*time
            y+=dy*time
            if time_to_horizontal<time_to_vertical:
                next_horizontal+= vertical
                oy+=vertical
            else:
                next_vertical+=horizontal
                ox += horizontal
    
    solution = list(filter(
        lambda x: 0<=x[0]<columns and 0<=x[1]<rows,
        solution
    ))
    return solution            
        




     
