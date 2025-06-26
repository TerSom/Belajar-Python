def tambah(*args):
    ouput = 0
    for data in args:
        ouput += data
        
    return ouput

def kali(*args):
    ouput = 1
    for data in args:
        ouput *= data
    
    return ouput

def pangkat(n:int):
    return lambda angka:angka**n