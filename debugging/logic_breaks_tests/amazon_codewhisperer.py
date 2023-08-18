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


def test_health_index():
    assert (health_index(70) == 40)
    assert (health_index(100) == 50)
    assert (health_index(80) == 60)
    assert (health_index(120) == 70)
    assert (health_index(50) == 70)
    assert (health_index(10) == 70)
    assert (health_index(5) == 70)
    assert (health_index(1) == 70)
    assert (health_index(0) == 70)
    print('YOUR CODE IS CORRECT!')


test_health_index()
