#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# NIM Designer/Coder : 16519074
# NIM Tester : 16519174

# f08- Penggunaan Tiket
def pakai_tiket(user,username,miliktiket,gunatiket,wahana):
    # Cari indeks dimana username ada di file
    FoundUser = False
    m = 0 # indeks cari row data user dengan username yang dicari
    while (FoundUser == False and user[m] != None):
        if (user[m][3] == username):
            FoundUser = True
        else:
            m = m + 1
    
    ID = input("Masukkan ID wahana (XXX999): ")
    Found = False # Akan true jika ditemukan wahana dengan ID yang diinput
    i = 0
    while (Found == False and wahana[i] != None): #Mencari wahana dengan ID yang diinput
        if (wahana[i][0] == ID):
            Found = True
        else:
            i = i + 1
    if (Found == False): # Salah input ID
        print("Tidak ditemukan wahana dengan ID tersebut")
    else: #Found == True
        Tanggal = input("Masukkan tanggal hari ini (DD/MM/YYYY): ")
        JmlTiket = int(input("Jumlah tiket yang digunakan: "))
        
        validsyarat = False # akan true jika user memenuhi syarat permainan
        j = 0
        while (validsyarat == False):
            if (miliktiket[j][0] == user[m][3]): #cek apakah username sama dengan data
                if (miliktiket[j][1] == ID): #cek apakah ID wahana sesuai dengan yang diinput
                    if (JmlTiket <= miliktiket[j][2]): # Cek apakah jumlah tiket mencukupi
                        print("Terima kasih telah bermain.")
                        miliktiket[j][2] = miliktiket[j][2] - JmlTiket
                        if (miliktiket[j][2] == 0):
                            miliktiket[j] = None
                        # isi data penggunaan ke file gunatiket
                        foundmark = False
                        k = 0
                        while (foundmark == False):
                            if (gunatiket[k] == None):
                                foundmark = True
                            else:
                                k = k + 1
                        gunatiket[k] = [user[m][3],Tanggal,ID,JmlTiket]
                        # keluar dari loop
                        validsyarat = True
                    else:
                        break #jumlah tiket kurang
                else:
                    j = j + 1
            else:
                j = j + 1
        if (validsyarat == False):
            print("Tiket Anda tidak valid dalam sistem kami.")
    return

