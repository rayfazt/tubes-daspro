# F13 - Top Up Saldo
# NIM Coder: 16519384

import csv

# Prosedur melakukan topup saldo user
def topup(user):

    uname = input('Masukkan username: ')
    saldo = int(input('Masukkan saldo yang di-top up: '))  # Input saldo berupa integer

    # cek username
    i = 0
    while user[i][3] != uname:
        i += 1

    # proses penambahan saldo
    saldoawal = int(user[i][6])  # Perhitungan dilakukan dalam integer
    saldoakhir = int(saldo + saldoawal)
    user[i][6] = str(saldoakhir)  # Saldo disimpan kembali sebagai string

    print('Top up berhasil. Saldo ', uname, ' bertambah menjadi ', saldoakhir)
    return user

