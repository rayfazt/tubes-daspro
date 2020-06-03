# Tubes Willy Wangky | 2020 
# F07 - Pembelian Tiket
# NIM Coder : 16519074
# NIM Coder : 16519174

def beli_tiket(user,username,wahana,belitiket,miliktiket):
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
        JmlTiket = int(input("Jumlah tiket yang dibeli: "))
        harga = float(wahana[i][2]) # Harga wahana yang ingin dimainkan disimpan dalam variabel harga
        if (user[m][7] == "gold"): #jika user sudah golden account, harga tiket dibagi 2
            harga = harga/2
        # Cek persyaratan umur dan batasan tinggi dari user
        
        # Cek umur pemain sesuai tanggal hari ini dan tanggal ulang tahun user
        umurpemain = int(Tanggal[6:10])-int(user[m][1][6:10])
        if (int(Tanggal[3:5]) <= int(user[m][1][3:5])):
            if (int(Tanggal[:2]) < int(user[m][1][:2])):
                umurpemain = umurpemain - 1
                
        tinggipemain = int(user[m][2])
        
        validsyarat = True # akan false jika user tidak memenuhi syarat permainan
        if (wahana[i][3] == "anak-anak"):
            if (umurpemain >= 17): # Mengecek apakah umur pemain sesuai
                validsyarat = False
            else: # umurpemain sesuai, yaitu <17 tahun
                if (wahana[i][4] == ">=170"): # Tidak perlu dicek untuk tinggi badan tanpa batasan karena pasti valid
                    if (tinggipemain < 170): #Mengecek apakah tinggi badan user >= 170 cm
                        validsyarat = False
        if (wahana[i][3] == "dewasa"):
            if (umurpemain < 17): # Mengecek apakah umur pemain sesuai
                validsyarat = False
            else: # umurpemain sesuai, yaitu >=17 tahun
                if (wahana[i][4] == ">=170"):
                    if (tinggipemain < 170): #Mengecek apakah tinggi badan user >= 170 cm
                        validsyarat = False
        if (wahana[i][3] == "semua umur"): # Tidak perlu dicek umur karena pasti valid
                if (wahana[i][4] == ">=170"):
                    if (tinggipemain < 170): #Mengecek apakah tinggi badan user >= 170 cm
                        validsyarat = False
        if (validsyarat == False):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini")
            print("Silakan menggunakan wahana lain yang tersedia.")
        else: #validsyarat == True
            # Cek apakah saldo mencukupi
            
            if (float(user[m][6]) < (float(JmlTiket)*(harga))): #Saldo kurang dari harga tiket
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda ")
            else: # Saldo cukup
                wahana[i][5] = int(wahana[i][5]) + JmlTiket # Jumlah tiket terjual untuk wahana tersebut bertambah
                user[m][6] = float(user[m][6]) - (float(JmlTiket)*harga) #mengurangi jumlah saldo
                k = 0 # indeks untuk file belitiket
                j = 0 # indeks untuk file kepemilikan tiket
                FoundMarkBeli = False # Mencari indeks terakhir ditemukan data pada file beli tiket
                FoundMarkMilik = False # Mencari indeks terakhir ditermukan data pada file milik tiket
                while (FoundMarkBeli == False):
                    if (belitiket[k] == None): #Ketemu baris di file yang kosong
                        belitiket[k] = [user[m][3],Tanggal,ID,JmlTiket] #Simpan data beli tiket ke file beli tiket
                        FoundMarkBeli = True
                    else:
                        k = k + 1
                while (FoundMarkMilik == False):
                    if (miliktiket[j] == None): #Ketemu baris di file yang kosong
                        miliktiket[j] = [user[m][3],ID,JmlTiket] #Simpan data kepemilikan tiket
                        FoundMarkMilik = True
                    elif (miliktiket[j][0] == user[m][3] and miliktiket[j][1] == ID): #ditemukan data kepemilikan sebelumnya dengan username dan ID wahana yang sama
                        miliktiket[j][2] = int(miliktiket[j][2]) + JmlTiket #jumlah tiket sebelumnya ditambah dengan yang dibeli
                        FoundMarkMilik = True
                    else:
                        j = j + 1
                print("Selamat bersenang-senang di " + wahana[i][1])
    return
