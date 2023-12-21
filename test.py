#Moduly

#Pizzerie
print('''
          ______           __                      ____  _                
         / ____/___ ______/ /________  ______     / __ \(_)_______  ____ _
        / /_  / __ `/ ___/ __/ ___/ / / / __ \   / /_/ / /_  /_  / / __ `/
       / __/ / /_/ (__  ) /_/ /  / /_/ / / / /  / ____/ / / /_/ /_/ /_/ / 
      /_/    \__,_/____/\__/_/   \__,_/_/ /_/  /_/   /_/ /___/___/\__,_/  
    ''')
print("                         Vítejte ve Fastrun Pizza")

pays = str(input("Chcete vidět ceník?\n")).lower()
if pays =="ano":
     print("Ceníky pizz jsou:\n Malá (S) = 100Kč\n Střední (M) = 150Kč\n Velká (L) = 200Kč\n")
     print("Příplatky jsou:\n Feferonky = 20/30/40Kč\n Sýrový okraj = 30/40/50Kč\n Doprava = 15/15/15Kč\n(Příplatky jsou uvedeny vždy podle velikostí pizz Malá/Střední/Velká)\n")
    


import modul  
print("Děkujeme za návštěvu Fastrun Pizza")