is_even=lambda x:x%2==0
is_odd=lambda x:x%2!=0

def get_lcm(x,y):
    greater=0
    lcm=0
    if x>y:
         greater=x
    elif x<y:
        greater=y
    else:
        lcm=x
        return lcm
    
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    
    return lcm

def get_hcf(x,y):
    return int( (x*y)/get_lcm(x,y) )

def get_factors(x):
    factors=list()
    for i in range(1,x+1):
        if x%i==0:
            factors.append(i)
    return factors

def is_prime(x):
    if len(get_factors(x))==2:
        return True
    else:return False

def factorial(x):
    if x==1 or x==0:
        return 1
    elif x>1:
        return x*factorial(x-1)

def is_perfect(x):
    if sum(get_factors(x))-x==x:
        return True
    else:return False

def is_palindrome(x):
    revx=str(x)
    revx=revx[::-1]
    if revx==str(x):
        return True
    else:
        return False

def is_armstrong(x):
    digits=list(str(x))
    power_digits=list(map(lambda i:int(i)**len(digits),digits))
    if sum(power_digits)==x:
        return True
    else:return False

def no_of_combinations(n,r):
    if n>=r and r>=0:
        return int( factorial(n)/( factorial(r)*factorial(n-r) ))

def no_of_permutations(n,r):
    if n>=r and r>=0:
        return int( factorial(n)/factorial(n-r) )
