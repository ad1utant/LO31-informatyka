import random
runnning = True
MENU = '''
z           - zakończ
ob          - generuje obelgę
dp          - dodaje przymiotnik
wp          - wyświetl przymiotniki
wr          - wyświetl rzeczowniki
dr          - dodaje rzeczownik 
ur <sample> - usuwa rzeczownik
up <sample> - usuwa przymiotnik
'''
print(MENU)
p,r = [],[]
while runnning:
    answer = input().lower()



    if answer == 'z':
        runnning = False


    if answer == 'ob':
        if len(p) == 0 or len(r) == 0:
            print('nie dodales zadnych rzeczownikow lub przymiotnikow')
        else:
            print(random.choice(p),random.choice(r))



    if answer == 'dp' or answer == 'dr':
        print('wpisz element: ')
        x = input().lower()
        if x not in p and answer == 'dp':
            p.append(x)
        if x not in r and answer == 'dr':
            r.append(x)
        elif x in p or x in r:
            print('element jest już dodany')
        else:
            print('wystąpił błąd')

    if answer == 'wp':
        for i in range(len(p)):
            print(p[i])

    if answer == 'wr':
        for i in range(len(r)):
            print(r[i])

    if answer == 'ur':
        x = input().lower()
        if x in r:
            r.remove(x)
        if x not in r:
            print('nie ma takiego rzeczownika')
    if answer == 'up':
        x = input().lower()
        if x in p:
            p.remove(x)
        if x not in p:
            print('nie ma takiego przymiotnika')

