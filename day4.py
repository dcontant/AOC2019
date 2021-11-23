def test1(n):
    flag1,flag2 = True,False
    for i in range(0,5):
        a,b = n[i:i+2]
        if a>b:
            flag1 = False
            break
        if a==b:
            flag2 = True
    return flag1 and flag2

def test2(n):
    flag1, flag2 = True, False
    for i in range(5):
        a,b = n[i:i+2]
        if a>b:
            flag1 = False
            break
        if a==b:
            if i==0 and n[2]!=a:
                flag2 = True
            elif i in [1,2,3] and a not in (n[i-1],n[i+2]):
                flag2 = True
            elif i==4 and n[3]!=a:
                flag2 = True
    return flag1 and flag2


  
part1 = sum(test1((str(n))) for n in range(125730,579381+1))

part2 = sum(test2((str(n))) for n in range(125730,579381+1))

print(f'part1= {part1}  part2= {part2}')
