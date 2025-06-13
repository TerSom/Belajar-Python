# ++++++3---------10++++++

inputAngka = float(input("masukan angka \nnkurang dari 3 \natau \nlebih dari 10\n ="))

# ++++++3------
kurangDari = inputAngka < 3
# print (kurangDari)

# -----------10+++++++
lebihDari = inputAngka > 10
# print(lebihDari)

# ++++++3---------10++++++
isBenar = kurangDari or lebihDari
print(isBenar)



print(30*"=")
print(30*"=")
print(30*"=")

# -------3+++++++10-------

inputAngka = float(input("masukan angka \nnkurang dari 3 \natau \nlebih dari 10\n ="))

# --------3++++++
lebihDari = inputAngka > 3
# print(lebihDari)

# ++++++++10--------
kurangDari = inputAngka < 10
# print(kurangDari)

isBenar = lebihDari and kurangDari 
print(isBenar)
