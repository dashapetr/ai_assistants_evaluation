def health_index(age):
    if age > 70:
        return 40
    elif age > 100:
        return 50
        if age > 80:
            return 60
    else:
        return 70


# fix the bug in the code above

def health_index(age):
    if age > 100:
        return 50
    elif age > 80:
        return 60
    elif age > 70:
        return 40
    else:
        return 70

# Test the function with some example ages
test_ages = [65, 75, 85, 105]
results = [(age, health_index(age)) for age in test_ages]
results
