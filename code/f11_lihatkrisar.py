# Tubes Willy Wangky | 2020
# F11 - Melihat Kritik dan Saran   
# NIM Coder: 16519044
# NIM Tester : 16519384
 
def view_kritiksaran(kritiksaran):
    print("Kritik dan saran:")
    for i in range (1,1000):
        if (kritiksaran [i] != None) :
            print(str(kritiksaran[i][2]) + " | " + str(kritiksaran[i][1])+ " | " + str(kritiksaran[i][0]) + " | " + str(kritiksaran[i][3]))
        else:
            break