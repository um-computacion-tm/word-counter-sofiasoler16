import unittest
def palabra(pala):
    dicc = {}
    r = pala.split(" ")
    for d in r:
        cantpala = r.count(d) #el count cuenta cantidad de veces de una palabra, no cantidad de palabras
        key, value = d, cantpala
        dicc[key] = value

    return (dicc)
# la funcion cuenta cantidad de palabras, si hay 2 repetidas las cuenta como 1

    
if __name__ == "__main__":
    unittest.main()
    




