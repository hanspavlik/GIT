print("Vítejte v kalkulačce BMI")
weight = float(input("Zadejte vaši váhu v kilogramech: "))
height = float(input("Zadejte vaši výšku v centimetrech: "))
height = height / 100

bmi = weight / height**2
bmi = round(bmi,2)

print(f"Vaše BMI je {bmi}")
if bmi < 18.5:
    print("Trpíte podváhou")
elif 18.5 < bmi < 24.9:
    print("Vaše BMI je normální")
elif 25 < bmi < 29.9:
    print("Trpíte nadváhou")
elif 30 < bmi < 34.9:
    print("Trpíte obezitou")
else: 
    print("Trpíte silnou obezitou")
print("Děkuji za použití moji BMI kalkulačky")
