import unittest
def palabra(pala):
    r = pala.split(" ")
    for d in r:
        cantpala = r.count(d) #cuenta cantidad de veces de una palabra, no cantidad de palabras
        if cantpala >= 2:
            r.remove(d)
    cant = len(r)
    return (cant)



    
if __name__ == "__main__":
    unittest.main()


    




