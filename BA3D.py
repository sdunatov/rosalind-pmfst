def deBrujinGraph(k, text):
    D = {}
    for i in range(0, len(text) - k + 1):
        first = text[i : (i + k - 1)]
        second = text[(i + 1) : (i + k)]
        #ako first nije među kljucevima od D dodaj first kao kljuc, a second kao njegov value
        if first not in D:
            D[first] = [second]
        #ako je first kljuc u D onda mu u value dodaj second 
        else:
            D[first].append(second)
      
    out = ""
    keys = sorted(D.keys())
    for first in keys:
        second = ",".join(sorted(D[first]))
         #f(format) je tu kako nam se ne bi ispisalo {first} -> {second}\n
        out = out + f"{first} -> {second}\n"
    return print(out)
