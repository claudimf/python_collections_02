usurarios_data_science = [15, 23, 43, 56]
usurarios_machine_learning = [13, 23, 43, 56]

assistiram = []

assistiram = usurarios_data_science.copy()
assistiram.extend(usurarios_machine_learning)
print(assistiram)

print(set(assistiram))

assistiram2 = list(set(assistiram))

print(assistiram2)

print(type({1,2}))


usurarios_data_science = {15, 23, 43, 56}
usurarios_machine_learning = {13, 23, 43, 56}

print(usurarios_data_science | usurarios_machine_learning)

print(usurarios_data_science & usurarios_machine_learning)
