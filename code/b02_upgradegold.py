# B02 - Golden Account
# NIM Coder: 16519384

import csv

# Prosedur melakukan upgrade status user ke golden account
def upgrade_gold(user):

    uname = input('Masukkan username yang ingin di-upgrade: ')

    # searching username
    i = 0 
    while user[i][3] != uname:
        i += 1
    
    # proses upgrade
    saldo = int(user[i][6])
    if saldo - 350000 >= 0:   # Harga akun gold adalah 350000
        user[i][7] = 'gold'
        user[i][6] = str(saldo - 350000)
        print('Akun Anda telah diupgrade.')
    else:   # saldo tidak cukup
        print('Saldo tidak cukup. Anda kekurangan sejumlah ', 350000 - saldo, ' untuk upgrade.')
    
    return user
