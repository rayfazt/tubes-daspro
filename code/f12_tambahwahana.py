# Tubes Willy Wangky | 2020
# F12 - MENAMBAHKAN WAHANA BARU
# NIM Coder : 16519114
# NIM Tester : 16519384

def tambah_wahana(wahana):
    mark = None
    #global wahana

    # Menerima input pengguna (asumsi semua valid)

    print("Masukkan Informasi Wahana yang ditambahkan:")

    idw = str(input("Masukkan ID Wahana (XXX999): "))
    nmw = str(input("Masukkan Nama Wahana: "))
    hrg = int(input("Masukkan Harga Tiket: "))
    btu = str(input("Batasan umur: "))
    btb = str(input("Batasan tinggi badan: "))

    # Memasukkan input pengguna
    i = 0
    while (i <= 1000) and (wahana[i] != mark):
        i = i + 1
    
    wahana[i] = [idw, nmw, hrg, btu, btb, 0]
    print("\nInfo wahana telah ditambahkan!")