# membuat program list buku

listbuku = []
while True:
    judulBuku = ""
    penulis = ""

    while not judulBuku:
        judulBuku = input("masukan judul buku = ")
        if not judulBuku:
            print("judul buku harus di isi")
            
    while not penulis:
        penulis = input("masukan penulis  = ")
        if not penulis:
            print("penulis buku harus di isi")

    bukuBaru = [judulBuku,penulis]
    listbuku.append(bukuBaru)
    print("\n",10*"=","\n")
    for index,buku in enumerate(listbuku):
        print(f"No {index + 1} | Judulbuku {buku[0]} | penulis {buku[1]}")
    
    isLanjut =input("mau lanjut atau selesai (y/n) = ")
    if isLanjut == "n":
        break

print("program selesai")