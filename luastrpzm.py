
#BootAnimation2
print("""  _                      _                     _                   
 | |                    | |                   (_)                  
 | | _   _   __ _  ___  | |_  _ __  _ __  ____ _  _   _  _ __ ___  
 | || | | | / _` |/ __| | __|| '__|| '_ \|_  /| || | | || '_ ` _ \ 
 | || |_| || (_| |\__ \ | |_ | |   | |_) |/ / | || |_| || | | | | |
 |_| \__,_| \__,_||___/  \__||_|   | .__//___||_| \__,_||_| |_| |_|
                                   | |                             
                                   |_|                             """)
print("create by aaionx")
print("")

#interface
print("---------------------------------------------------")
print("Formula trpzium = 1/2 * (a + b) * h")
print("ISI NOMBOR BAGI MENGIRA LUAS TRAPEZIUM :")
print("---------------------------------------------------")

#Body
def kira():
    a = float()
    while True:
        a = float(input("masukkan nilai sisi selari a :"))
        print("")
        if a == int(0):
            print("")
            print("Have a nice day;)")
            break
        else:
          b = float(input("masukkan nilai sisi selari b :"))
          print("")
          h = float(input("masukkan nilai h :"))
          ab = float(a + b)
          luas = float(round(0.5 * ab * h, 2))
          print("Hasil Kira = ", luas ,"cm/m2")
          print("---------------------------------------------------")          
kira()

   

#end interface
print("")
print("")
print("---------------------------------------------------")
