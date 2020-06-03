# F03 - Save file
# NIM Coder: 16519384

import csv

# Prosedur menyimpan file csv
def save(user, wahana, belitiket, gunatiket, miliktiket, refund, kritiksaran):

    nmax = 1000
   
    # File User
    file_user = input('Masukkan nama File User: ')
    with open(file_user, 'w', newline='') as datauser:
        write = csv.writer(datauser, delimiter = ',')
        i = 0
        for i in range(nmax):
            if user[i] != None: # Data akan ditulis selama isi array bukan None
                write.writerow(user[i])
            i += 1
    # File Wahana
    file_wahana = input('Masukkan nama File Daftar Wahana: ')
    with open(file_wahana, 'w', newline='') as datawahana:
        write = csv.writer(datawahana, delimiter = ',')
        i = 0
        for i in range(nmax):
            if wahana[i] != None:
                write.writerow(wahana[i])
            i += 1
    # File Pembelian Tiket
    file_beli = input('Masukkan nama File Pembelian Tiket: ')
    with open(file_beli, 'w', newline='') as databeli:
        write = csv.writer(databeli, delimiter = ',')
        i = 0
        for i in range(nmax):
            if belitiket[i] != None:
                write.writerow(belitiket[i])
            i += 1
    # File Penggunaan Tiket  
    file_guna = input('Masukkan nama File Penggunaan Tiket: ')
    with open(file_guna, 'w', newline='') as dataguna:
        write = csv.writer(dataguna, delimiter = ',')
        i = 0
        for i in range(nmax):
            if gunatiket[i] != None:
                write.writerow(gunatiket[i])
            i += 1
    # File Kepemilikan Tiket
    file_milik = input('Masukkan nama File Kepemilikan Tiket: ')
    with open(file_milik, 'w', newline='') as datamilik:
        write = csv.writer(datamilik, delimiter = ',')
        i = 0
        for i in range(nmax):
            if miliktiket[i] != None:
                write.writerow(miliktiket[i])
            i += 1
    # File Refund Tiket
    file_refund = input('Masukkan nama File Refund Tiket: ')
    with open(file_refund, 'w', newline='') as datarefund:
        write = csv.writer(datarefund, delimiter = ',')
        i = 0
        for i in range(nmax):
            if refund[i] != None:
                write.writerow(refund[i])
            i += 1
    # File Kritik Saran
    file_kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
    with open(file_kritiksaran, 'w', newline='') as datasaran:
        write = csv.writer(datasaran, delimiter = ',')
        i = 0
        for i in range(nmax):
            if kritiksaran[i] != None:
                write.writerow(kritiksaran[i])
            i += 1
    
    print('Data berhasil disimpan!')
    return user,wahana,belitiket,gunatiket,miliktiket,refund,kritiksaran
