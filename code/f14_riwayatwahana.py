# Tubes Willy Wangky | 2020
# F14 - MELIHAT RIWAYAT PENGGUNAAN WAHANA
# NIM Coder : 16519114
# NIM Tester : 16519114

def riwayat_wahana(penggunaan):
    mark = None
    #global penggunaan

    # Menerima input pengguna (asumsi pasti benar)

    idw = str(input("Masukkan ID wahana (XXX999): "))

    # Menuliskan riwayat penggunaan wahana

    print("Riwayat:")

    found = False
    i = 0

    while (i <= 1000) and (penggunaan[i] != mark):
        if (penggunaan[i][2] == idw):
            print(penggunaan[i][1] + " | " + penggunaan[i][0] + " | " + str(penggunaan[i][3]))
            found = True
        i = i + 1
    
    if not(found):
        print("Tidak ada riwayat penggunaan tiket.")