def lower_left_triangle(x,y,s,k=" "):
    for i in range(x):
        for j in range(y):
            if i>=j:
                print(s,end=" ")
            else:
                print(k,end=" ")
        print()

def upper_left_triangle(x,y,s,k=" "):
    for i in range(1,x+1):
        for j in range(y,0,-1):
            if i<=j:
                print(s,end=" ")
            else:
                print(k,end=" ")
        print()

def upper_right_triangle(x,y,s,k=" "):
    for i in range(x):
        for j in range(y):
            if i<=j:
                print(s,end=" ")
            else:
                print(k,end=" ")
        print()

def lower_right_triangle(x,y,s,k=" "):
    for i in range(1,x+1):
        for j in range(y,0,-1):
            if i>=j:
                print(s,end=" ")
            else:
                print(k,end=" ")
        print()
    
def boundary(x,y,s,k=" "):
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i==1 or j==1 or i==x or j==y:
                print(s,end=" ")
            else:
                print(k,end=" ") 
        print()

def left_diagonal(x,y,s,k=" "):
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i==j:
                print(s,end=" ")
            else:
                print(k,end=" ") 
        print()

def right_diagonal(x,y,s,k=" "):
    for i in range(1,x+1):
        for j in range(y,0,-1):
            if i==j:
                print(s,end=" ")
            else:
                print(k,end=" ")
        print()

def num_horizontal(x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(j,end=" ")
        print()

def num_vertical(x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(i,end=" ")
        print()

def diagonal_digit(x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i==j:
                print(i,end=" ")
            else:
                print(" ",end=" ")
        print()