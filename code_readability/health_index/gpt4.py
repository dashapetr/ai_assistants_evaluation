# calculate health index: it is 40 for a person aged more than 70;
# 50 for a person aged 50-69; 60 for a person aged 40-49; 70 for a person aged before 40

def health_index(age):
    """Calculate the health index based on age."""
    if age > 70:
        return 40
    elif 50 <= age <= 69:
        return 50
    elif 40 <= age <= 49:
        return 60
    elif age < 40:
        return 70
    else:
        raise ValueError("Invalid age input.")

# Test the function with sample ages
sample_ages = [20, 45, 55, 71, 69, 40]
health_indices = [health_index(age) for age in sample_ages]
health_indices
