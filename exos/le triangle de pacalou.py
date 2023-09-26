def pascalou(n,p):
    if n == p or p == 0:
        return 1
    else:
        return pascalou(n-1,p)+pascalou(n-1,p-1)


print(pascalou(6,2))