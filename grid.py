from time import sleep
def main(input):
    r2=input
    r1=[]
    while r1!=r2:
         print ('\n')
         r1=process(r2)
         sleep(1)
         printer(r1)
         r2=process (r1)
         sleep(1)
         print('\n')
         printer(r2)
    print ("OVER")
def process(grid):
    l=len(grid[0])
    
    count=0
    result=demo(l)
    for i in range(l):
        
        for j in range(l):
            count=0
            x=i-1
            y=j-1
            k=0
            for k in range(3):
                
                for z in range (3):
                    if x >= 0 and y >=0 and x<l and y<l :
                        if grid[x][y]==1:
                            count+=1
                            
                    y+=1
                            
                x+=1
                z=0
                y=j-1
            
            if is_alive(grid,i,j)==True:
                count-=1
                if count in (2,3):
                    result[i][j]=1
            elif is_alive(grid,i,j)==False:
                
                if count ==3:
                    result[i][j]=1
            
    return (result)



def is_alive(ip,i,j):
    if ip[i][j]==1:
        return True
    else:
        return False

def demo(l):
    result=[]
    for i in  range (l):
        result.append([0]*l)
    return (result)

def printer(op):
    for i in op:
        for j in i:
            if j ==1:
                print '#',
            else:
                print '.',
        print "\n"
