# Tubes Willy Wangky | 2020
# B04 - LAPORAN KEHILANGAN TIKET
# NIM Coder : 16519114
# NIM Tester : 16519044

def tiket_hilang(miliktiket):
    # global miliktiket
    # Menerima input pengguna (asumsi pasti valid)
    idp = str(input("Masukkan username: "))
    tgl = str(input("Tanggal kehilangan tiket (DD/MM/YYYY): "))
    idw = str(input("ID wahana (XXX999): "))
    jml = int(input("Jumlah tiket yang dihilangkan: "))

    # Mencari jumlah tiket yang dimiliki pengguna
    i = 0
    found = False
    while (miliktiket[i] != None) and (not(found)):
        if (miliktiket[i][0] == idp) and (miliktiket[i][1] == idw):
            found = True
        else:
            i += 1

    # Pengurangan tiket
    if (found):
        miliktiket[i] = (miliktiket[i][0], miliktiket[i][1], str(int(miliktiket[i][2]) - jml))
        print("Laporan kehilangan tiket Anda telah direkam.")
    else:
        print("Maaf ada data yang Anda masukkan tidak dapat ditemukan.")