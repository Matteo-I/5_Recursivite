def middle(point_A, point_B):
    """
    Retourne le milieu du point A et B
    
    Parameters:
    
    point_A : un tuple de 2 nombres (Xa, Ya)
    point_B : un tuple de 2 nombres (Xb, Yb)
    
    Return:
    le milieu de A et B : un tuple de 2 nombres
    """
    xm=(point_A[0]+point_B[0])/2
    ym=(point_A[1]+point_B[1])/2
    return(xm,ym)