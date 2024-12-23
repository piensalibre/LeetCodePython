import unittest
from romanToInt import RomanToInt

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.converter = RomanToInt()

    def test_basic_numerals(self):
        self.assertEqual(self.converter.romanToInt("I"), 1)
        self.assertEqual(self.converter.romanToInt("V"), 5)
        self.assertEqual(self.converter.romanToInt("X"), 10)
        self.assertEqual(self.converter.romanToInt("L"), 50)
        self.assertEqual(self.converter.romanToInt("C"), 100)
        self.assertEqual(self.converter.romanToInt("D"), 500)
        self.assertEqual(self.converter.romanToInt("M"), 1000)

    def test_combinations(self):
        self.assertEqual(self.converter.romanToInt("II"), 2)
        self.assertEqual(self.converter.romanToInt("III"), 3)
        self.assertEqual(self.converter.romanToInt("IV"), 4)
        self.assertEqual(self.converter.romanToInt("IX"), 9)
        self.assertEqual(self.converter.romanToInt("XL"), 40)
        self.assertEqual(self.converter.romanToInt("XC"), 90)
        self.assertEqual(self.converter.romanToInt("CD"), 400)
        self.assertEqual(self.converter.romanToInt("CM"), 900)

    def test_complex_numbers(self):
        self.assertEqual(self.converter.romanToInt("LVIII"), 58)  # L + V + III
        self.assertEqual(self.converter.romanToInt("MCMXCIV"), 1994)  # M + CM + XC + IV
        self.assertEqual(self.converter.romanToInt("MMMCMXCIX"), 3999)  # MMM + CM + XC + IX

    def test_edge_cases(self):
        self.assertEqual(self.converter.romanToInt(""), 0)  # Vacío
        self.assertEqual(self.converter.romanToInt("MMMM"), 4000)  # Valores más allá de los límites típicos

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
