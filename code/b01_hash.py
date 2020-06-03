# Tubes Willy Wangky | 2020
# B01 - Penyimpanan Password
# NIM Code : 16519174
# NIM Tester : 16519074

import hashlib # Modul untuk hashing
import binascii # Modul covert Binary-ASCII
import os # Digunakan untuk generate angka random

def hashPassword(password):
    # Generate salt/ bagian random dari hashed password
    salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii')
        # hashlib.sha256() : Encode salt dengan SHA-256
        # hexdigest() : Mengembalikan string dengan length 64 dan berisi hanya digit hexadecimal
        # os.urandom() : Generate string yang berisi character random
        # encode() : Ubah string menjadi bytes

    # Menghash password
    hashed_password = hashlib.pbkdf2_hmac('sha512', # Encode password dengan SHA-512
                                        password.encode('ascii'), # Password dicovert jadi bytes
                                        salt, # Salt yang sudah digenerate
                                        100000) # Iterasi SHA-256 sebanyak 100,000 kali
    hashed_password = binascii.hexlify(hashed_password) # Mengubah hashed_password menjadi bentuk hexadecimalnya

    return (salt + hashed_password).decode('ascii')

def verifyPassword(stored_password, input_password):
    # Mengambil salt
    salt = stored_password[:64]
    # Mengubah stored_password menjadi bagian passwordnya saja
    stored_password = stored_password[64:]

    # Mengubah input_password menjadi versi hashed
    hashed_password = hashlib.pbkdf2_hmac('sha512', # Encode password dengan SHA-512
                                        input_password.encode('ascii'), # Password dicovert jadi bytes
                                        salt.encode('ascii'), # Salt diencode menjadi ascii
                                        100000) # Iterasi SHA-256 sebanyak 100,000 kali
    hashed_password = binascii.hexlify(hashed_password).decode('ascii') # Mengubah hashed_password menjadi bentuk hexadecimalnya

    return hashed_password == stored_password




