def find_median(vetor_base, k, vetor, list_palpites = []):
    if len(vetor) > 5:
        mom = []
        i = 0
        while i < len(vetor):
            mom.append(find_median(vetor_base, k, vetor[i:i + 5], list_palpites))
            i += 5
        if len(mom) <= 5:
            return check(vetor_base, find_median(vetor_base, k, mom, list_palpites), k, list_palpites)
        else:
            return find_median(vetor_base, k, mom, list_palpites)
    else:
        vetor.sort()
        if len(vetor) % 2 == 0:
            return vetor[int((len(vetor) / 2)) - 1]
        else:
            return vetor[int((len(vetor) - 1) / 2)]


def check(vetor_base, palpite, k, list_palpites = []):
    list_palpites.append(palpite)

    l = []
    r = []
    for i in vetor_base:
        if i < palpite:
            l.append(i)
        elif i > palpite:
            r.append(i)
    if len(l) == k - 1:
        return list_palpites
    elif len(l) < k:
        if len(r) <= 5:
            r.sort()
            if len(r) % 2 == 0:
                return check(r, r[int((len(r) / 2)) - 1], k - len(l) - 1, list_palpites)
            else:
                return check(r, r[int((len(r) - 1) / 2)], k - len(l) - 1, list_palpites)
        else:
            return find_median(r, k - len(l) - 1, r)
    else:
        if len(l) <= 5:
            l.sort()
            if len(l) % 2 == 0:
                return check(l, l[int((len(l) / 2)) - 1], k, list_palpites)
            else:
                return check(l, l[int((len(l) - 1) / 2)], k, list_palpites)
        else:
            return find_median(l, k, l)