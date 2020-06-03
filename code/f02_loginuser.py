# Tubes Willy Wangky | 2020
# F04 Login User
# NIM Coder : 16519174
# NIM Tester : 16519074

from b01_hash import verifyPassword

def login(user):
    # Login
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Searching Username & Cek Password
    found = False
    i = 0
    while(user[i] != None):
        if ((user[i][3] == username) and (verifyPassword(user[i][4], password))):
            found = True
            
            # Memasukkan role user
            user_role = user[i][5]
            break
        else:
            i += 1

    # Output Message
    if (found):
        print("Selamat bersenang-senang,", user[i][0],"!" )
        return (username, user_role)
    else:
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        return True

            



