# calculate health index: it is 40 for a person aged more than 70;
# 50 for a person aged 50-69; 60 for a person aged 40-49; 70 for a person aged before 40

def health_index(age):
    if age > 70:
        return 40
    elif age > 50:
        return 50
    elif age > 40:
        return 60
    else:
        return 70


print(health_index(80))
print(health_index(60))
print(health_index(45))
print(health_index(30))
