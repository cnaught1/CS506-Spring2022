def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res

def jaccard_dist(x, y):
    res = 0
    if x==y:
        res = 0
    else:
        intersection = len(list(set(x).intersection(y)))
        union = len(x)
        res = 1-float(intersection)/union
    return res

def cosine_sim(x, y):
    res=0
    if x==y:
        res = 1
    else:
        dotproduct=0
        normX=0
        normY=0
        for a,b in zip(x,y):
            dotproduct = dotproduct+a*b
        for i in x:
            normX += (i ** 2)**(1/2)
        for j in y:
            normY += (j ** 2)**(1/2)
        if normX ==0 or normY ==0:
            res=0
        else:
            res = dotproduct/(normX*normY)
    return res

# Feel free to add more
