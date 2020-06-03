# Tubes Willy Wangky | 2020
# F15 - MELIHAT JUMLAH TIKET PEMAIN
# NIM Coder : 16519114
# NIM Tester : 16519044

def tiket_pemain(miliktiket, wahana):
    mark = None
    #global miliktiket
    #global wahana

    # Menerima input pengguna (asumsi pasti benar)

    idp = str(input("Masukkan username: "))

    # Menuliskan jumlah tiket yang dimiliki pemain

    print("Riwayat:")

    i = 0
    found = False

    while (i <= 1000) and (miliktiket[i] != mark):
        if (miliktiket[i][0] == idp):
            # Mencari nama wahana menurut kode wahana
            j = 0
            while miliktiket[i][1] != wahana[j][0]:
                j = j + 1
            # Menuliskan data yang didapat
            print(miliktiket[i][1] + " | " + wahana[j][1] + " | " + str(miliktiket[i][2]))
            found = True
        i = i + 1
    
    if not(found):
        print("Tidak ada riwayat kepemilikan tiket.")