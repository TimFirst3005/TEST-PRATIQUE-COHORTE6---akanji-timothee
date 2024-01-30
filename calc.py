def calc(array, n_1, n_2):
    res = 0
    # Contraintes sur les parametres
    if n_1 < 0 or n_2<0:
        print("Vous avez renseigné {} et {} inférieurs à 0".format(n_1, n_2))
    if n_1>n_2:
        print("{} doit être inferieur ou égal à {}".format(n_1, n_2))
    if n_2> len(array):
        print("{} doit être inferieur ou égal à {}".format(n_2,len(array)))
        
    #   implementation de la somme
    for i in range(n_1, n_2+1):
        res += array[i]
    return res