# cotoh exception 
from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harung angka"
    return a+b     

print(tambah(10,a))