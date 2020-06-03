# Tubes Willy Wangky | 2020
# F09 - REFUND
# NIM Coder : 16519114
# NIM Tester : 16519174

def refund(username,user,wahana,miliktiket,refundtiket):
    mark = None
    #global user
    #global wahana
    #global miliktiket
    #global refundtiket
    
    # Menerima input pengguna

    idp = username
    
    # Mencari akun user
    k = 1
    while (user[k][3] != idp):
        k = k + 1

    # Mencari wahana
    found = False

    j = 1
    idw = str(input("Masukkan ID wahana (XXX999): "))
    while not(found) and (j < 1000) and (wahana[j] != mark):
        if (wahana[j][0] == idw):
            found = True
        else: j = j + 1

    while not(found):
        j = 1
        print("\nID wahana tidak ditemukan.")
        idw = str(input("Masukkan ID wahana (XXX999): "))
        while not(found) and (j < 1000) and (wahana[j] != mark):
            if (wahana[j][0] == idw):
                found = True
            else: j = j + 1
            
    tgl = input("Masukkan tanggal hari ini (DD/MM/YYYY): ")
    jml = input("Jumlah tiket yang di-refund: ")
    while not(jml.isnumeric()):
            print("\nJumlah tiket harus berupa angka.")
            jml = input("Jumlah tiket yang di-refund: ")
    
    jml = int(jml)


    # Mencari jumlah tiket yang dimiliki pemain

    i = 1
    tiket = 0
    found = False

    while not(found) and (i <= 1000) and (miliktiket[i] != mark):
        if (miliktiket[i][0] == idp) and (miliktiket[i][1] == idw):
            found = True
            tiket = int(miliktiket[i][2])
        else: i = i + 1

    # Jika memiliki cukup tiket

    if tiket >= jml:
        print("Uang refund sudah kami berikan pada akun Anda.")
        
        # Proses refund ke akun user
        miliktiket[i] = (miliktiket[i][0], miliktiket[i][1], int(miliktiket[i][2]) - jml)
        user[k] = (user[k][0], user[k][1], user[k][2], user[k][3], user[k][4], user[k][5], float(user[k][6]) + (0.5 * jml * float(wahana[j][2])), user[k][7])

        # Menuliskan riwayat refund
        l = 1
        while (refundtiket[l] != mark):
            l = l + 1
        refundtiket[l] = (username, tgl, idw, jml)

    # Jika tidak memiliki cukup tiket

    else:
        print("Anda tidak memiliki tiket terkait.")