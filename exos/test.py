def rfact(n):
    return n*rfact(n-1) #appel récursif, la variable n décroit
    
rfact(4)