'''
cek total harga printer
created by Eduardus sare (20083000026)
    kelas 2A
'''
import os
clear = lambda : os.system('cls')
jwb = "y"

while jwb == "Y" or jwb == "y" :
    clear()
    print("PROGRAM HITUNG TOTAL HARGA PRINTER EPSON T20")
    print("--------------------------------------------")
    
    hrgPrinter = 660000
    a = input("Masukkan Jumlah Printer = ")
    jmlhPrinter = int(a)
    

    totHrg = hrgPrinter * jmlhPrinter
    print()
    print ("Total Harga = Rp.",format(totHrg,",.2f"))

    
    print()
    jwb = input("Cek Lagi? (y/t) = ")
    if jwb == "t" or jwb == "T" :
        break
