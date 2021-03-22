usurarios_data_science = {15, 23, 43, 56}
usurarios_machine_learning = {13, 23, 43, 56}

# Utilizar o | para juntar conjuntos
print(usurarios_data_science | usurarios_machine_learning)

# Utilizar o & para juntar apenas números que estão no mesmo conjunto
print(usurarios_data_science & usurarios_machine_learning)

# Utilizar o - para remover números repetidos que estão no em dois conjuntos
print(usurarios_data_science - usurarios_machine_learning)

# ou (^) exclusivo
print(usurarios_data_science ^ usurarios_machine_learning)