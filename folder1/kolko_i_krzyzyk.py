def wskaz_zwyciesce(plansza):
    # wiersze
    for i in range(3):
        if plansza[i][0] == plansza[i][1] == plansza[i][2]:
            return plansza[i][0]

    # kolumny
    for i in range(3):
        if plansza[0][i] == plansza[i][1] == plansza[i][2]:
            return plansza[0][i]

    # przekatne
    if plansza[0][0] == plansza[1][1] == plansza[2][2] or\
            plansza[0][2] == plansza[1][1] == plansza[2][0]:
        return plansza[1][1]

    # remis
    else:
        return ""


print(wskaz_zwyciesce([['o', 'o', 'x'], ['o', 'x', 'o'], ['x', 'x', 'o']]))
