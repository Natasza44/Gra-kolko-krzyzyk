def wpisz_i_zwroc_wartosc():
    choose_one = input("choose one 'x' or 'o' and row and column:")
    wartosci = choose_one.split(' ')

    if len(wartosci) != 3:
        print('Try again')
        return None

    wariant = wartosci[0]
    rzad = wartosci[1]
    kolumna = wartosci[2]

    if poprzedni_wariant == [] and wariant not in ['o']:
        print('"o" should be first!')
        return None
    if wariant not in ['o', 'x']:
        print('Try again!')
        return None
    elif rzad not in ['1','2','3']:
        print('Try again!')
        return None
    elif kolumna not in ['1','2','3']:
        print('Try again!')
        return None
    else:
        return [wariant, int(rzad), int(kolumna)]

def sprawdzanie_wygranej(row1,row2,row3):
    Brak_wygranej = True
    if (row1[0] == row2[0] == row3[0] != ' '):
        Brak_wygranej = False
        print(row1[0] + ' You won! :D')
    elif (row1[1] == row2[1] == row3[1] != ' '):
        Brak_wygranej = False
        print(row1[1] + ' You won! :D')
    elif (row1[2] == row2[2] == row3[2] != ' '):
        Brak_wygranej = False
        print(row1[2] + ' You won! :D')
    elif (row1[0] == row1[1] == row1[2] != ' '):
        Brak_wygranej = False
        print(row1[0] + ' You won! :D')
    elif (row2[0] == row2[1] == row2[2] != ' '):
        Brak_wygranej = False
        print(row2[0] + ' You won! :D')
    elif (row3[0] == row3[1] == row3[2] != ' '):
        Brak_wygranej = False
        print(row3[0] + ' You won! :D')
    elif (row1[0] == row2[1] == row3[2] != ' '):
        Brak_wygranej = False
        print(row1[0] + ' You won! :D')
    elif (row3[0] == row2[1] == row1[2] != ' '):
        Brak_wygranej = False
        print(row3[0] + ' You won! :D')
    elif (row1[0] != ' ' and row1[1] != ' ' and row1[2] != ' '
          and row2[0] != ' ' and row2[1] != ' ' and row2[2] != ' '
          and row3[0] != ' ' and row3[1] != ' ' and row3[2] != ' '):
        Brak_wygranej = False
        print('The game ended in a draw! :)')
    return Brak_wygranej


def display (row1,row2,row3):
    print (row1)
    print (row2)
    print (row3)


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
wszystkie_rzedy = [row1, row2, row3]


Brak_wygranej = True
poprzedni_wariant = []


while Brak_wygranej:

    rezultat = wpisz_i_zwroc_wartosc()

    if rezultat is None:
        continue

    wariant = rezultat[0]
    rzad = rezultat[1]
    kolumna = rezultat[2]


    if poprzedni_wariant == wariant:
        print(f'Opps! {wariant} it is not your turn! :/')
        continue

    if wszystkie_rzedy[rzad - 1][kolumna - 1] != ' ':
        print('Opps! This place is filled! :(')
        continue

    if rzad == 1:
        row1[kolumna-1] = wariant
    elif rzad == 2:
        row2[kolumna-1] = wariant
    elif rzad == 3:
        row3[kolumna-1] = wariant

    poprzedni_wariant = wariant

    display(row1, row2, row3)
    Brak_wygranej = sprawdzanie_wygranej(row1,row2,row3)

    if Brak_wygranej:
        continue
    else:
        odpowiedz = input('Do you want to try again? Yes/No')
        if odpowiedz.lower() == "yes":
            Brak_wygranej = True
            row1 = [' ', ' ', ' ']
            row2 = [' ', ' ', ' ']
            row3 = [' ', ' ', ' ']
            wszystkie_rzedy = [row1, row2, row3]
            poprzedni_wariant = []




