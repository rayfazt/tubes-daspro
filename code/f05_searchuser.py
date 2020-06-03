# Tubes Willy Wangky | 2020
# F05 - Pencarian Pemain
# NIM Coder : 16519174
# NIM Tester : 16519074

def cari_pemain(user):
    # Input user
    username = input("Masukkan username: ")

    # Searching Username & Cek Password
    found = False
    i = 0
    while(user[i] != None):
        if (username == user[i][3]):
            found = True
            break
        else:
            i += 1
    
    # Output Message
    if (found):
        print("Nama Pemain:", user[i][0])
        print("Tinggi Pemain:", user[i][2], "cm")
        print("Tanggal Lahir Pemain:", user[i][1])
    else:
        print("Ups, username tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        cari_pemain(user)