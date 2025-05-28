# tipe data: angka satuan yang gk ada
# koma nya (integer)

data_interger = 10
print("data :", data_interger)
print("- bertipe", type(data_interger))

data_float = 1.2
print("data :", data_float)
print("- bertipe", type(data_float))

data_String = "terry kelas"
print("data :", data_String)
print("- bertipe", type(data_String))

data_bool = False
print("data :", data_bool)
print("- bertipe", type(data_bool))

# tipe data khusus

data_komplex = complex(6,5)
print("data :", data_komplex)
print("- bertipe", type(data_komplex))

# tipe data dari bahasa c

from ctypes import c_double,c_char


data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe", type(data_c_double))



