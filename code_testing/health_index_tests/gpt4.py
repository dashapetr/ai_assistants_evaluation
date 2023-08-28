# after the health index fuction creation, I asked GPT4 to create test cases
# and run them in current environment

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

# Writing test cases for the health_index function
class TestHealthIndex(unittest.TestCase):

    def test_above_70(self):
        self.assertEqual(health_index(80), 40)
        self.assertEqual(health_index(100), 40)
        self.assertEqual(health_index(71), 40)

    def test_50_to_69(self):
        self.assertEqual(health_index(50), 50)
        self.assertEqual(health_index(55), 50)
        self.assertEqual(health_index(69), 50)

    def test_40_to_49(self):
        self.assertEqual(health_index(40), 60)
        self.assertEqual(health_index(45), 60)
        self.assertEqual(health_index(49), 60)

    def test_below_40(self):
        self.assertEqual(health_index(20), 70)
        self.assertEqual(health_index(0), 70)
        self.assertEqual(health_index(39), 70)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            health_index(-1)


# Executing the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestHealthIndex)
unittest.TextTestRunner().run(suite)


# The tests for the health_index function mostly passed, but there was one failure.
# The test case test_invalid_age failed because the function did not raise a ValueError
# when provided with a negative age.
# To address this, we need to modify the health_index function to handle negative age inputs.

def health_index(age):
    """Calculate the health index based on age."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 70:
        return 40
    elif 50 <= age <= 69:
        return 50
    elif 40 <= age <= 49:
        return 60
    else:
        return 70  # for age < 40

# Rerunning the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestHealthIndex)
unittest.TextTestRunner().run(suite)

# All tests for the health_index function now pass successfully.
# The modification to handle negative ages resolved the previous failure.
# The function is now confirmed to work correctly for the tested cases.
