def kSortingReversal(P, k):
    j = k
    while P[j] != k+1 and P[j] != -(k+1):
        j += 1 
    P[k:(j+1)] = list(map(Funkcija,P[k:(j+1)][::-1]))
    return P
        
def Funkcija(x):
    return -x
    
def GreedySorting(P):
    P = P.strip().replace("(","").replace(")","").split()
    niz = []
    for p in P:
        niz.append(int(p))
    for k in range(0, len(niz)):
        if niz[k] != k+1:
            niz = kSortingReversal(niz, k)
            print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in niz])+")")
            if niz[k] == -(k+1):
                niz = kSortingReversal(niz, k)
                print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in niz])+")")
