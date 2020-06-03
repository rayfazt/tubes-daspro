# Tubes Willy Wangky | 2020
# Main File
# KELOMPOK 2 IF1210 K-04

# IMPORT FITUR SPESIFIKASI PROGRAM
from f01_load import load
from f02_loginuser import login
from f03_save import save
from f04_signupuser import signup
from f05_searchuser import cari_pemain
from f06_pencarianwahana import cari_wahana
from f07_pembeliantiket import beli_tiket
from f08_menggunakantiket import pakai_tiket
from f09_refund import refund
from f10_tambahkrisar import add_kritiksaran
from f11_lihatkrisar import view_kritiksaran
from f12_tambahwahana import tambah_wahana
from f13_topup import topup
from f14_riwayatwahana import riwayat_wahana
from f15_tiketpemain import tiket_pemain
from f16_exit import exit_program

# IMPORT FITUR SPESIFIKASI BONUS
from b02_upgradegold import upgrade_gold
from b03_bestwahana import best_wahana
from b04_laporhilangtiket import tiket_hilang

# FUNGSI MAIN MENU
def admin_main_menu():
    print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N           ADMIN |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Selamat datang di Wahana Bermain Willy Wangky!             |
            |  Apa yang ingin anda lakukan sekarang?                      |
            |                                                             |
            |  0 EXIT                      6 LIHAT KRITIK&SARAN           |
            |  1 SAVE FILE                 7 TAMBAH WAHANA                | 
            |  2 SIGN UP USER              8 TOP UP SALDO                 |
            |  3 CARI PEMAIN               9 RIWAYAT WAHANA               |
            |  4 CARI WAHANA               10 JUMLAH TIKET                | 
            |  5 CARI BEST WAHANA          11 UPGRADE ACCOUNT             | 
            |                                                             |
            |  Mohon untuk memasukkan nomor menu                          |
            |  sesuai yang anda inginkan.                                 |
            +-------------------------------------------------------------+
    """)
    menu = int(input("Fitur apa yang ingin anda gunakan?: "))
    found = False
    while not(found):
        if (menu == 0):
            #0 EXIT
            print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N                 |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Terima kasih atas kunjangan anda di Wahana Bermain Willy   | 
            |  Wangky! Semoga anda akan datang kembali.                   | 
            +-------------------------------------------------------------+
            """)
            exit_program(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
            found = True
        elif (menu == 1):
            #1 SAVE FILE
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Program akan mulai untuk save file.                        |
            +-------------------------------------------------------------+
            """)
            save(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
            admin_main_menu()
            found = True
        elif (menu == 2):
            #2 SIGN UP USER
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan untuk mengisi data dibawah ini untuk sign up.     |
            +-------------------------------------------------------------+
            """)
            signup(user)
            admin_main_menu()
            found = True
        elif (menu == 3):
            #3 CARI PEMAIN
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi username pemain yang ingin dicari.            |
            +-------------------------------------------------------------+
            """)
            cari_pemain(user)
            admin_main_menu()
            found = True
        elif (menu == 4):
            #4 CARI WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk mencari wahana.            |
            +-------------------------------------------------------------+
            """)
            cari_wahana(wahana)
            admin_main_menu()
            found = True
        elif (menu == 5):
            #5 CARI BEST WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Berikut adalah daftar 3 besar wahana terbaik kami.         |
            +-------------------------------------------------------------+
            """)
            best_wahana(wahana)
            admin_main_menu()
            found = True
        elif (menu == 6):
            #6 LIHAT KRITIK&SARAN
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Berikut adalah daftar kritik dan saran wahana.             |
            +-------------------------------------------------------------+
            """)
            view_kritiksaran(kritiksaran)
            admin_main_menu()
            found = True
        elif (menu == 7):
            #7 TAMBAH WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk menambah wahana baru.      |
            +-------------------------------------------------------------+
            """)
            tambah_wahana(wahana)
            admin_main_menu()
            found = True
        elif (menu == 8):
            #8 TOP UP SALDO
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk melakukan top up saldo.    |
            +-------------------------------------------------------------+
            """)
            topup(user)
            admin_main_menu()
            found = True
        elif (menu == 9):
            #9 RIWAYAT WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan masukkan ID wahana untuk melihat riwayat wahana.  |
            +-------------------------------------------------------------+
            """)
            riwayat_wahana(gunatiket)
            admin_main_menu()
            found = True
        elif (menu == 10):
            #10 JUMLAH TIKET
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi username untuk melihat tiket pemain.          |
            +-------------------------------------------------------------+
            """)
            tiket_pemain(miliktiket,wahana)
            admin_main_menu()
            found = True
        elif (menu == 11):
            #11 UPGRADE ACCOUNT
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Mohon siapkan saldo sebesar Rp350.000 untuk mengupgrade    |
            |  akun menjadi Golden Account.                               |
            |  Silahkan isi username pemain yang ingin diupgrade.         |
            +-------------------------------------------------------------+
            """)
            upgrade_gold(user)
            admin_main_menu()
            found = True
        else :
            print("Mohon masukkan hanya angka antara 0 - 11.")
            menu = int(input("Fitur apa yang ingin anda gunakan?: "))

def pemain_main_menu():
    print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N          PEMAIN |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Selamat datang di Wahana Bermain Willy Wangky!             |
            |  Apa yang ingin anda lakukan sekarang?                      |
            |                                                             |
            |  0 EXIT                        5 PAKAI TIKET                |
            |  1 SAVE FILE                   6 REFUND                     |
            |  2 CARI WAHANA                 7 BERI KRITIK & SARAN        |
            |  3 CARI BEST WAHANA            8 RIWAYAT WAHANA             | 
            |  4 BELI TIKET                  9 LAPOR HILANG TIKET         |
            |                                                             |
            |  Mohon untuk memasukkan nomor menu                          |
            |  sesuai yang anda inginkan.                                 |
            +-------------------------------------------------------------+
    """)
    menu = int(input("Fitur apa yang ingin anda gunakan?: "))
    found = False
    while not(found):
        if (menu == 0):
            #0 EXIT
            print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N                 |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Terima kasih atas kunjangan anda di Wahana Bermain Willy   | 
            |  Wangky! Semoga anda akan datang kembali.                   | 
            +-------------------------------------------------------------+
            """)
            exit_program(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
            found = True
        elif (menu == 1):
            #1 SAVE FILE
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Program akan mulai untuk save file.                        |
            +-------------------------------------------------------------+
            """)
            save(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
            pemain_main_menu()
            found = True
        elif (menu == 2):
            #2 CARI WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk mencari wahana.            |
            +-------------------------------------------------------------+
            """)
            cari_wahana(wahana)
            pemain_main_menu()
            found = True
        elif (menu == 3):
            #3 CARI BEST WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Berikut adalah daftar 3 besar wahana terbaik kami.         |
            +-------------------------------------------------------------+
            """)
            best_wahana(wahana)
            pemain_main_menu()
            found = True
        elif (menu == 4):
            #4 BELI TIKET
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk membeli tiket.             |
            +-------------------------------------------------------------+
            """)
            beli_tiket(user,username,wahana,belitiket,miliktiket)
            pemain_main_menu()
            found = True
        elif (menu == 5):
            #5 PAKAI TIKET
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk bermain di wahana!         |
            +-------------------------------------------------------------+
            """)
            pakai_tiket(user,username,miliktiket,gunatiket,wahana)
            pemain_main_menu()
            found = True
        elif (menu == 6):
            #6 REFUND
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk melakukan refund.          |
            +-------------------------------------------------------------+
            """)
            refund(username,user,wahana,miliktiket,refundtiket)
            pemain_main_menu()
            found = True
        elif (menu == 7):
            #7 BERI KRITIK & SARAN
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi form berikut untuk memberikan kritik/saran.   |
            +-------------------------------------------------------------+
            """)
            add_kritiksaran(username, kritiksaran)
            pemain_main_menu()
            found = True
        elif (menu == 8):
            #8 RIWAYAT WAHANA
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan masukkan ID wahana untuk melihat riwayat wahana.  |
            +-------------------------------------------------------------+
            """)
            riwayat_wahana(gunatiket)
            pemain_main_menu()
            found = True
        elif (menu == 9):
            #9 LAPOR HILANG TIKET
            print("""
            +-------------------------------------------------------------+
            |  Program Pembantu Wahana Bermain Willy Wangky.              |
            |  Silahkan isi data berikut untuk membuat laporan            |
            +-------------------------------------------------------------+
            """) 
            tiket_hilang(miliktiket)
            pemain_main_menu()
            found = True
        else :
            print("Mohon masukkan hanya angka antara 0 - 9.")
            menu = int(input("Fitur apa yang ingin anda gunakan?: "))

# ALGORITMA UTAMA
print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N                 |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Selamat datang di Wahana Bermain Willy Wangky!             |
            |  Program akan mulai untuk load file.                        |
            +-------------------------------------------------------------+
""")
files = load()
user = files[0]
wahana = files[1]
belitiket = files[2]
gunatiket = files[3]
miliktiket = files[4]
refundtiket = files[5]
kritiksaran = files[6]

print("""
            +-------------------------------------------------------------+
            |               W A H A N A     B E R M A I N                 |
            |   __      ___ _ _       __      __              _           |
            |   \ \    / (_) | |_  _  \ \    / /_ _ _ _  __ _| |___  _    |
            |    \ \/\/ /| | | | || |  \ \/\/ / _` | ' \/ _` | / / || |   |
            |     \_/\_/ |_|_|_|\_, |   \_/\_/\__,_|_||_\__, |_\_\ _, |   |
            |                   |__/                    |___/     |__/    |
            +-------------------------------------------------------------+
            |  Selamat datang di Wahana Bermain Willy Wangky!             |
            |  Mohon untuk melakukan login user terlebih dahulu.          | 
            +-------------------------------------------------------------+
""")

userinfo = login(user)
if (userinfo == True):
    while(True):
        userinfo = login(user)
        if (userinfo != True):
            break

username = userinfo[0]
user_role = userinfo[1]

if (user_role == 'admin') :
    admin_main_menu()
else:
    pemain_main_menu()

