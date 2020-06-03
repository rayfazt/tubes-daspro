# Tubes Willy Wangky | 2020
# F16 - EXIT
# NIM Coder: 16519044
# NIM Tester : 16519144

from f03_save import save

def exit_program(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran):
    opt_save = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if (opt_save == 'Y'):
        save(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
    elif (opt_save == 'N'):
        None
    else:
        print("Mohon untuk hanya menjawab dengan huruf Y atau N.")
        exit_program(user, wahana, belitiket, gunatiket, miliktiket, refundtiket, kritiksaran)
  
