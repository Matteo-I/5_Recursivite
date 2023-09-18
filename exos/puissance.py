def puissance(a,b):
    if b==0:
        return 1
    else:
        return a*puissance(a,b-1)
    
print(puissance(2,983))