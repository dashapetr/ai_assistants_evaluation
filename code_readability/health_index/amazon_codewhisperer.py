# calculate health index: it is 40 for a person aged more than 70;
# 50 for a person aged 50-69; 60 for a person aged 40-49; 70 for a person aged before 40


age = int(input("Enter your age: "))

if age > 70:
    print("Health index: 40")

elif age >= 50:
    print("Health index: 50")

elif age >= 40:
    print("Health index: 60")

else:
    print("Health index: 70")
