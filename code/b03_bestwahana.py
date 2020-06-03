# Tubes Willy Wangky | 2020
# B03 - Best Wahana
# NIM Designer/Coder : 16519074
# NIM Tester : 16519384

def best_wahana(wahana):
    best1 = wahana[1] #inisialisasi 3 variabel awal dengan jumlah tiket terjual 3 wahana pertama
    best2 = wahana[2]
    best3 = wahana[3]
    # mengurutkan best1,best2,best3 menjadi maksimum secara menurun dengan best1 maksimum terbesar dan best3 maksimum terkecil
    if(int(best1[5]) > int(best2[5]) and int(best1[5]) > int(best3[5])): # jika best1 maksimum
        if(int(best3[5]) > int(best2[5])): #jika best3 > best2
            temp = best3
            best3 = best2
            best2 = temp
    if(int(best2[5]) > int(best1[5]) and int(best2[5]) > int(best3[5])): # jika best2 maksimum
        temp = best1
        best1 = best2
        best2 = temp
        if (int(best3[5]) > int(best2[5])): #jika best3 > best1
            temp = best3
            best3 = best2
            best2 = temp
    if(int(best3[5]) > int(best1[5]) and int(best3[5]) > int(best2[5])): # jika best3 maksimum
        temp = best1
        best1 = best3
        best3 = temp
        if(int(best3[5]) > int(best2[5])): # jika best1 > best2
            temp = best3
            best3 = best2
            best2 = temp
    
    # Mencari nilai maksimum di indeks lain
    i = 4
    while(wahana[i] != None): # sampai data berakhir
        if(int(wahana[i][5]) >= int(best1[5])): # jika data yang dicek lebih besar dari best1
            temp1 = best1
            temp2 = best2
            best1 = wahana[i] # best1 jadi wahana yang dicek
            best2 = temp1 #best1 bergeser ke best2
            best3 = temp2 #best2 bergeser ke best3
            i = i + 1
        elif(int(wahana[i][5]) < int(best1[5]) and int(wahana[i][5]) >= int(best2[5])): #jika wahana yang dicek lebih kecil dari best1 tapi lebih besar dari best2
            temp = best2
            best2 = wahana[i] # best2 menjadi wahana yang dicek
            best3 = temp #best2 bergeser ke best3
            i = i + 1
        elif(int(wahana[i][5]) < int(best2[5]) and int(wahana[i][5]) >= int(best3[5])): # jika wahana yang dicek lebih kecil dari best2 tapi lebih besar dari best3
            best3 = wahana[i] # best3 ditukar dengan wahana yang dicek
            i = i + 1
        else: #wahana yang dicek lebih kecil dari best3
            i = i + 1
            
    print("1 | " + best1[0] + " | " + best1[1] + " | " + str(best1[5]))
    print("2 | " + best2[0] + " | " + best2[1] + " | " + str(best2[5]))
    print("3 | " + best3[0] + " | " + best3[1] + " | " + str(best3[5]))
    
    return
    

