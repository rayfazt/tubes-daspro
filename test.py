import csv

def load():     # Prosedur memuat file csv ke program
    user = input('Masukkan nama File User: ')
    with open('user.csv') as csvfile:
        read = csv.reader(csvfile)
        user = []
        for row in read:
            user.append(row)
    wahana = input('Masukkan nama File Daftar Wahana: ')
    with open('wahana.csv') as csvfile:
        read = csv.reader(csvfile)
        wahana = []
        for row in read:
            wahana.append(row)
    pembelian = input('Masukkan nama File Pembelian Tiket: ')
    with open('pembelian.csv') as csvfile:
        read = csv.reader(csvfile)
        pembelian = []
        for row in read:
            pembelian.append(row)
    penggunaan = input('Masukkan nama File Penggunaan Tiket: ')
    with open('penggunaan.csv') as csvfile:
        read = csv.reader(csvfile)
        penggunaan = []
        for row in read:
            penggunaan.append(row)
    tiket = input('Masukkan nama File Kepemilikan Tiket: ')
    with open('tiket.csv') as csvfile:
        read = csv.reader(csvfile)
        tiket = []
        for row in read:
            tiket.append(row)
    refund = input('Masukkan nama File Refund Tiket: ')
    with open('refund.csv') as csvfile:
        read = csv.reader(csvfile)
        refund = []
        for row in read:
            refund.append(row)
    kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
    with open('kritiksaran.csv') as csvfile:
        read = csv.reader(csvfile)
        kritiksaran = []
        for row in read:
            kritiksaran.append(row)
    
    print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran

load()

#def topup():    # Prosedur melakukan topup saldo user
   # with open('user.csv') as csvfile:
