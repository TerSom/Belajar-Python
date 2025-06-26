from matematika import tambah as TAMBAH
from matematika import kali as KALI
from matematika import pangkat as PANGKAT

import matematika as math

print(math.tambah(10,10))

hasil_tambah = TAMBAH(1,2,3,4,5)
print(f"hasil tambah {hasil_tambah}")

hasil_kali = KALI(1,2,3,4,5)
print(f"hasil kali {hasil_tambah}")

hasil_pangkat = PANGKAT(2)
print(f"hasil pangkat {hasil_pangkat(2)}")