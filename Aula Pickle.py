import pickle
pratos = [10000, 2, 3]

with open('pratos.pkl', 'wb') as file:
    prato = pickle.dump(pratos, file)

