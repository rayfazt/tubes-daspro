# Tubes Willy Wangky | 2020 
# F06 - Cari wahana
# NIM Coder : 16519074
# NIM Tester : 16519174

def cari_wahana(wahana):
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()
    umur = int(input("Batasan umur pemain: "))
    while (umur != 1 and umur != 2 and umur != 3): #Cek apakah input umur valid
        print("Batasan umur tidak valid!")
        umur = int(input("Batasan umur pemain: "))
    tinggi = int(input("Batasan tinggi badan: "))
    while (tinggi != 1 and tinggi != 2): #cek apakah input tinggi valid
        print("Batasan tinggi badan tidak valid!")
        tinggi = int(input("Batasan tinggi badan: "))
    AdaWahana = False #Jika ditemukan wahana sesuai, nilainya menjadi True
    
    # Cari jumlah wahana dalam file
    Mark = False
    indeks = 0
    while (Mark == False):
        if (wahana[indeks] == None): # Barisan ke-indeks kosong
            Mark = True
        else:
            indeks = indeks + 1
    #         
    if (umur == 1):
        if (tinggi == 1):
            for i in range(indeks):
                if (wahana[i][3] == "anak-anak" and wahana[i][4] == ">=170"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
        else: # tinggi == 2
            for i in range(indeks):
                if (wahana[i][3] == "anak-anak" and wahana[i][4] == "tanpa batasan"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
    elif (umur == 2):
        if (tinggi == 1):
            for i in range(indeks):
                if (wahana[i][3] == "dewasa" and wahana[i][4] == ">=170"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
        else: # tinggi == 2
            for i in range(indeks):
                if (wahana[i][3] == "dewasa" and wahana[i][4] == "tanpa batasan"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
    else: # umur == 3
        if (tinggi == 1):
            for i in range(indeks):
                if (wahana[i][3] == "semua umur" and wahana[i][4] == ">=170"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
        else: # tinggi == 2
            for i in range(indeks):
                if (wahana[i][3] == "dewasa" and wahana[i][4] == "tanpa batasan"):
                    print(wahana[i][0] + " | " + wahana[i][1] + " | " + wahana[i][2])
                    AdaWahana = True
    if(AdaWahana == False): #Tidak ditemukan wahana
        print("Tidak ada wahana yang sesuai dengan pencarian kamu")
    return
