import numpy as np

ankgaList = [1,2,3,4]
numpyList = np.array([1,2,3,4])

print(f"angkalist = {ankgaList}" )
# print(ankgaList**2) angka list tidak bisa di pangkat atau di kalis
print(f"numpyList = {numpyList}" )
print(numpyList**2) # kalo numpy bisa

matrix_a = np.array([(2,3),(2,3)])
print(matrix_a)

matrix_zero = np.zeros([2,2])
print(matrix_zero)

matrix_ones = np.ones([2,2])
print(matrix_ones)

tambah_matrix = matrix_a + matrix_ones
print(tambah_matrix)