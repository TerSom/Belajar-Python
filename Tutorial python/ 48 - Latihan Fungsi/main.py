import os

def header():
    os.system('clear')
    """Header untuk program menghitung luas dan keliling persegi panjang."""
    print("="*50)
    print("Program Menghitung Luas dan Keliling Persegi Panjang")
    print("="*50)
    
def inputUser():
    """fungsing untuk input data dari user."""
    lebar = float(input("Masukkan Lebar Persegi Panjang: "))
    panjang = float(input("Masukkan Panjang Persegi Panjang: "))
    return lebar, panjang

def hitungLuas(lebar,panjang):
    """Fungsi untuk menghitung luas persegi panjang."""
    return lebar * panjang

def hitungKeliling(lebar,panjang):
    """Fungsi untuk menghitung keliling persegi panjang."""
    return 2 * (lebar + panjang)

def display(message,value):
    """Fungsi untuk menampilkan pesan dan nilai."""
    print(f"message: {message} = {value}")
    


while True:
    header()
    LEBAR,PANJANG = inputUser()
    LUAS = hitungLuas(LEBAR,PANJANG)
    KELILING = hitungKeliling(LEBAR,PANJANG)
    display("Luas Persegi Panjang", LUAS)
    display("Keliling Persegi Panjang", KELILING)

    isDone = input("Apakah Anda ingin menghitung luas dan keliling persegi panjang? (y/n): ")
    if isDone == "n":
        print("Terima kasih telah menggunakan program ini!")
        break
    
print("Program selesai.")