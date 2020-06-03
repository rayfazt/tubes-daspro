# Tubes Willy Wangky | 2020 
# F04 - Sign Up User
# NIM Coder : 16519174
# NIM Tester : 16519074

from b01_hash import hashPassword

def user_available(username, user):
    # Check username
    found = False
    i = 0
    while(user[i] != None):
        if (username == user[i][3]):
            found = True
            break
        else:
            i += 1
        
    if (found) :
        return False
    else :
        return True

def signup(user):
    # Sign Up
    # Validasi input nama pemain
    while(True):
        nama_pemain = input("Masukkan nama pemain: ")
        if all((char.isalpha()) or (char.isspace()) for char in nama_pemain):
            break
        else :
            print("Mohon untuk hanya menggunakan huruf alphabet dalam menulis nama.")

    # Input Tanggal Lahir
    ttl = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")

    # Validasi input tinggi badan
    while(True):
        tinggi = input("Masukkan tinggi badan pemain (cm): ")
        if (tinggi.isnumeric()):
            break
        else :
            print("Mohon untuk memasukkan tinggi badan dalam cm dan angka.")
    
    # Check Availibility Username
    while(True):
        username = input("Masukkan username pemain: ")
        if (user_available(username, user)):
            break
        else :
            print("Username sudah digunakan. Mohon gunakan username lainnya.")

    # Input Password
    password = input("Masukkan password pemain: ")
    password = hashPassword(password)

    # Data dimasukkan ke dalam file
    empty = True
    i = 0
    while(empty):
        if (user[i] == None):
            user[i] = [nama_pemain, ttl, tinggi, username, password, "player", 0, "standard"]
            empty = False
        i += 1

    return user, print("Selamat menjadi pemain, ", nama_pemain, ".Selamat bermain.")
