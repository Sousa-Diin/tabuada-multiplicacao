print("_______________TABUADA DE MULTIPLICAÇÃO______________")
print('example: tabuada [1] | tabuada [2] ....')
tabu = int(input('Digite qual tabuada deseja exibir: '))

mult_tabu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mult_tabu:
    print(tabu, 'X', mult_tabu[i], ': {}'.format(tabu * mult_tabu[i]))
