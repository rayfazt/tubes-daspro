# F01 - Load file
# NIM Coder: 16519384

import csv

# Prosedur memuat file csv ke program
def load():
    
    nmax = 1000     # Asumsi indeks maksimum array adalah 1000
    
    # File User
    file_user = input('Masukkan nama File User: ')
    user = [None for i in range(nmax)]  # Deklarasi array
    with open(file_user, 'r') as datauser:
        read = csv.reader(datauser, delimiter = ',')
        i = 0
        for row in read:    # Mengisi data csv  ke array
            user[i] = row
            i += 1
    # File Wahana
    file_wahana = input('Masukkan nama File Daftar Wahana: ')
    wahana = [None for i in range(nmax)]
    with open(file_wahana, 'r') as datawahana:
        read = csv.reader(datawahana, delimiter=',')
        i = 0
        for row in read:
            wahana[i] = row
            i += 1
    # File Pembelian Tiket
    file_beli = input('Masukkan nama File Pembelian Tiket: ')
    belitiket = [None for i in range(nmax)]
    with open(file_beli, 'r') as databeli:
        read = csv.reader(databeli, delimiter = ',')
        i = 0
        for row in read:
            belitiket[i] = row
            i += 1
    # File Penggunaan Tiket  
    file_guna = input('Masukkan nama File Penggunaan Tiket: ')
    gunatiket = [None for i in range(nmax)]
    with open(file_guna, 'r') as dataguna:
        read = csv.reader(dataguna, delimiter = ',')
        i = 0
        for row in read:
            gunatiket[i] = row
            i += 1
    # File Kepemilikan Tiket
    file_milik = input('Masukkan nama File Kepemilikan Tiket: ')
    miliktiket = [None for i in range(nmax)]
    with open(file_milik, 'r') as datamilik:
        read = csv.reader(datamilik, delimiter = ',')
        i = 0
        for row in read:
            miliktiket[i] = row
            i += 1
    # File Refund Tiket
    file_refund = input('Masukkan nama File Refund Tiket: ')
    refund = [None for i in range(nmax)]
    with open(file_refund, 'r') as datarefund:
        read = csv.reader(datarefund, delimiter = ',')
        i = 0
        for row in read:
            refund[i] = row
            i += 1
    # File Kritik Saran
    file_kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
    kritiksaran = [None for i in range(nmax)]
    with open(file_kritiksaran, 'r') as datasaran:
        read = csv.reader(datasaran, delimiter = ',')
        i = 0
        for row in read:
            kritiksaran[i] = row
            i += 1
    
    print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return user, wahana, belitiket, gunatiket, miliktiket, refund, kritiksaran



