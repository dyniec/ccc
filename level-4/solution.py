from fractions import Fraction as F

rows,columns = list(map(int,input().split()))
n= int(input())
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
        




     
for i in range(n):
    ox,oy,dx,dy=list(map(int,input().split()))
    result = one_test((ox,oy),(dx,dy))
    print(*[" ".join([str(x),str(y)]) for (x,y) in result])
