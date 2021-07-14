import random


def gera_tabuleiro():
    tab = []
    for i in range(9):
        tab_lin = []
        for j in range(9):
            tab_lin.append(0)
        tab.append(tab_lin)

    return(tab)


def mostra_tab(tab):
#imprime o tabuleiro de forma compreensiva
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")


def encontra_zero(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return (i, j)

    return None



def eh_valido(tab, num, pos):
    #checa linha
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    #checa coluna
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False

    # Checa quadrado
    quad_x = pos[1] // 3
    quad_y = pos[0] // 3

    for i in range(quad_y*3, quad_y*3 + 3):
        for j in range(quad_x * 3, quad_x*3 + 3):
            if tab[i][j] == num and (i,j) != pos:
                return False

    return True



def resolve(tab):
    encontra = encontra_zero(tab)
    #caso base
    if not encontra:
        return True
    else:
        linha, coluna = encontra

    for i in range(1,10):
        if eh_valido(tab, i, (linha, coluna)):
            tab[linha][coluna] = i

            if resolve(tab):
                return True

            tab[linha][coluna] = 0

    return False

def preenche_tab(tab):
    chances = [1,2,3,4,5,6,7,8,9]
    tab[0][0] = random.choice(chances)
    tab[2][2] = random.choice(chances)
    tab[8][8] = random.choice(chances)

    resolve(tab)
    for i in range(9):
        for j in range(9):
            sort = random.choice(chances)
            if sort <= 4:
                tab[i][j] = 0
    return tab

tabuleiro = gera_tabuleiro()
tabuleiro = preenche_tab(tabuleiro)

mostra_tab(tabuleiro)
resolve(tabuleiro)
print('\n\n')
mostra_tab(tabuleiro)
