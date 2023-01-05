#BootAnimation1
print("please input your username..")
c1 = input()

languages = ['checking','','10%','', '20%','','30%','', '' ,
             '40%','','50%','', '60%','','70%','', '80%' ,
             '','90%','', '' , '100%' ,'done']

print('Hold your nerves:)')

for lname in languages:
  print(lname)
  if (lname == 'done'):
    break
print('done')
    
#BootAnimation2
print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝""")
print("create by aaionx")
print("")

print("press enter to start...")

c = input()

#interface
print("---------------------------------------------------")
print("ISI NOMBOR BAGI MENGIRA ISIPADU BULATAN:")
print("---------------------------------------------------")

#Body
def kira2():
    jejari2 = float()
    while True:
        jejari2 = float(input("masukkan nilai jejari :"))
        if jejari2 == int(0):
            print("")
            print("Have a nice day;)")
            break
        else:
            jejari_2 = float(jejari2 * jejari2 * jejari2)
            bulatan2 = float(round(1.33333 * 3.14159265359 * jejari_2, 2))
            print("Hasil Kira = ", bulatan2 ,"m^3")
            print("---------------------------------------------------")          
kira2()

   

#end interface
print("")
print("")
print("---------------------------------------------------")
