def health_index(age):
    if age > 70:
        return 40
    elif age > 50:
        return 50
    elif age > 40:
        return 60
    else:
        return 70


# create test cases for health index function

# test the health index function
assert health_index(80) == 40
assert health_index(60) == 50
assert health_index(45) == 60
assert health_index(30) == 70
assert health_index(20) == 70
assert health_index(10) == 70
assert health_index(5) == 70
assert health_index(0) == 70
assert health_index(-5) == 70
assert health_index(-10) == 70
assert health_index(-20) == 70
