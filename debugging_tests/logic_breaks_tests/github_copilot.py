def health_index(age):
    if age > 70:
        return 40
    elif age > 100:
        return 50
        if age > 80:
            return 60
    else:
        return 70


# code after the bug correction:


def health_index(age):
    if age > 100:
        return 60
    elif age > 80:
        return 50
    elif age > 70:
        return 40
    else:
        return 70
