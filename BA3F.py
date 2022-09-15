def EulerianCycle(adjacency_list):
    adj_list = adjacency_list.split('\n')
    D = {}
    for edge in adj_list:
        first, second = edge.split(" -> ")
        second = second.split(",")
        D[first] = second

    pocetni_cvor = list(D.keys())[0]
    trenutni_cvor = pocetni_cvor
    konacni_put = [pocetni_cvor]

    while D:
        if trenutni_cvor in D:
            konacni_put.append(D[trenutni_cvor][0])
            if len(D[trenutni_cvor]) == 1:
                del D[trenutni_cvor]
            else:
                del D[trenutni_cvor][0]
            trenutni_cvor = konacni_put[-1]
        else:
            for i, elem in enumerate(konacni_put):
                if elem in D:
                    novi_ciklus = konacni_put[i: -1] + konacni_put[:i + 1]
                    konacni_put = novi_ciklus
                    trenutni_cvor = elem
                    break

    res = "->".join(konacni_put)
    return res 
