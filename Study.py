#BootAnimation1
print("please input your username..")
username = input()

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
print("created by aaionx")
print("""
	
	 """)
print("Hello", username, "..")
print("""
	
	""")

print("press enter to start...")

c = input()

#interface1
print("---------------------------------------------------")
print("""Pilih pengiraan :
[1] mengira isipadu bulatan
[2] mengira luas trapezium
[3] mengira luas segi tiga
[4] matematik pengguna
[22] science archive""")
p = float(input("------>>"))


if p == int(1):
#isipadu bulatan
    print("---------------------------------------------------")
    print("ISI NOMBOR BAGI MENGIRA ISIPADU BULATAN:")
    print("---------------------------------------------------")   
    while True:
        jejari2 = float(input("masukkan nilai jejari :"))
        if jejari2 == int(0):
            print("")
            print("Have a nice day;)")
            break   
        else:
            jejari3 = float(jejari2 * jejari2 * jejari2)
            bulatan2 = float(round(1.33333 * 3.14159265359 * jejari3, 2))
            print("Hasil Kira = ", bulatan2 ,"m^3")
            print("---------------------------------------------------");
#luas trapezium         
elif p == int(2):
    print("---------------------------------------------------")
    print("ISI NOMBOR BAGI MENGIRA LUAS TRAPEZIUM :")
    print("---------------------------------------------------") 
    while True:
        a = float(input("masukkan nilai selari a :"))
        if a == int(0):
            print("Have a nice day=)")
            break
        else:         
            b = float(input("masukkan nilai selari b :"))
            h = float(input("masukkan nilai tinggi :"))
            luas = float(round(0.5 * (a + b) * h, 2))
            print("Luas =", luas, "m^2");            
#luas segitiga
elif p == int(3):
    print("---------------------------------------------------")
    print("ISI NOMBOR BAGI MENGIRA LUAS SEGITIGA :")
    print("---------------------------------------------------")
    while True:
        p = float(input("masukkan nilai panjang :" ))
        if p == int(0):
            print(" ")
            print("have a nice day=)")
            break
        else:
            t = float(input("masukkan nilai tinggi :"))
            luas = float(round(0.5 * p * t, 2))
            print("Luas =", luas , "m^2"); 
#kira simpanan dan pelaburan
elif p == int(4):
    print("---------------------------------------------------")
    print("""~matematik simpanan dan pelaburan~
pilih-pilih: 
[1]kira faedah mudah
[2]
[3]
[0]exit""")
    mn_mth = int(input("----->>"))    
    if mn_mth == int(1):        
        print("---------------------------------------------------")
        print("ISI NOMBOR BAGI MENGIRA Faedah( I = Prt):")
        print("---------------------------------------------------")      
        while True:                  
            prinsipal = float(input("masukkan prinsipal : RM"))
            if prinsipal == int(0):               
                print(" ")
                print("have a nice day0_0")
                break
            else:                          
                rate = float(input("masukkan peratus dalam perpuluhan :"))
                tahun = float(input("masukkan tahun :"))
                faedah = float(round(prinsipal * rate * tahun, 2))
                print("Faedah : ","RM",faedah)
                print("---------------------------------------------------");
    else:
       exit()
                     
        	               	    
            
#science formulae
elif p == int(22):
    print("""Pilih archive :
Science Daya       	
[1] formula mgh
[2] formula 1/2*fx
[3] formula 1/2*mv^2
[0] exit""")
    mn_sc = float(input("------>>"))
    print("---------------------------------------------------");
if mn_sc == int(1):
    print(" ")
    print("""pengenalan kepada mgh :
m = mass
g = gravity
h = height""");

elif mn_sc == int(2):
    print(" ")
    print("""pengenalan kepada 1/2*f*x :
        	f = daya(N)
        	x = kemampatan spring asal-spring mampat""");
        	
elif mn_sc == int(3):
    print(" ")
    print("""pengenalan kepada 1/2*mv^2 :
m = mass(kg)
v = velocity(halaju) dalam s^-2""");

elif mn_sc == int(0):
    print("Have a nice day0_0")
                 	        	        	        	                                                                                                       
print(" ")
print(" ")
print("---------------------------------------------------")
