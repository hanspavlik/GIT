size = str(input("Jakou velikost pizzy si přejete (S/M/L) ?\n")).lower()
bill = 0

if size == "s":
    bill += 100
    
    fef = str(input("Chcete na vaši pizzi feferonky?\n"))
    if fef == "ano":
        bill += 20
        print(f"Cena vaši pizzy je {bill}")
    else:
        print(f"Cena vaši pizzy je {bill}")    
    
    cheese = str(input("Chcete na vaši pizzu sýrový okraj?\n")).lower()
    if cheese == "ano":
            bill += 30
            print(f"Cena vaši pizzy je {bill}")
    else:
            print(f"Cena vaši pizzy je {bill}")
    
    delivery = str(input("Přejete si pizzu doručit?\n")).lower()
    if delivery == "ano":
        bill += 15
        print(f"Budete platit {bill}")
    else:
        print(f"Budete platit {bill}")

elif size == "m":
    bill += 150
    
    fef = str(input("Chcete na vaši pizzi feferonky?\n")).lower()
    if fef == "ano":
        bill += 30
        print(f"Cena vaši pizzy je {bill}")
    else:
        print(f"Cena vaši pizzy je {bill}")    
    
    cheese = str(input("Chcete na vaši pizzu sýrový okraj?\n")).lower()
    if cheese == "ano":
            bill += 40
            print(f"Cena vaši pizzy je {bill}")
    else:
            print(f"Cena vaši pizzy je {bill}")
    
    delivery = str(input("Přejete si pizzu doručit?\n")).lower()
    if delivery == "ano":
        bill += 15
        print(f"Budete platit {bill}")
    else:
        print(f"Budete platit {bill}")    
   
elif size == "l":
    bill += 200
    
    fef = str(input("Chcete na vaši pizzi feferonky?\n")).lower()
    if fef == "ano":
        bill += 40
        print(f"Cena vaši pizzy je {bill}")
    else:
        print(f"Cena vaši pizzy je {bill}")    
    
    cheese = str(input("Chcete na vaši pizzu sýrový okraj?\n")).lower()
    if cheese == "ano":
            bill += 50
            print(f"Cena vaši pizzy je {bill}")
    else:
            print(f"Cena vaši pizzy je {bill}")
    
    delivery = str(input("Přejete si pizzu doručit?\n")).lower()
    if delivery == "ano":
        bill += 15
        print(f"Budete platit {bill}")
    else:
        print(f"Budete platit {bill}")
    
else:
    print("Takovou velikost pizzy nemáme")