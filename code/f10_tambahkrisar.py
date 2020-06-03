# Tubes Willy Wangky | 2020
# F10 - Kritik dan Saran
# NIM Coder : 16519044
# NIM Tester : 16519384

def add_kritiksaran(username, kritiksaran) :
    idwahana = input("Masukkan ID Wahana: ")
    tanggal_kritik = input("Masukkan tanggal pelaporan (DD/MM/YYYY): ")
    kritik_saran = input ("Kritik/Saran Anda : ")

    temp = [username, tanggal_kritik, idwahana, kritik_saran]
    for i in range(1000) :
        if (kritiksaran[i] == None) :
            kritiksaran [i]= temp
            print ("Kritik dan saran Anda kami terima")
            break

