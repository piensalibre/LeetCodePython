import unittest
from isPalindrome import IsPalindrome

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = IsPalindrome()
    
    def test_positive_palindrome(self):
        # Caso donde el número es un palíndromo positivo
        self.assertTrue(self.solution.isPalindrome(121))

    def test_negative_number(self):
        # Caso donde el número es negativo, por lo tanto, no puede ser palíndromo
        self.assertFalse(self.solution.isPalindrome(-121))
    
    def test_non_palindrome(self):
        # Caso donde el número no es un palíndromo
        self.assertFalse(self.solution.isPalindrome(10))
    
    def test_single_digit(self):
        # Todos los números de un solo dígito son palíndromos
        self.assertTrue(self.solution.isPalindrome(0))
        self.assertTrue(self.solution.isPalindrome(7))
    
    def test_large_palindrome(self):
        # Caso donde el número es un palíndromo grande
        self.assertTrue(self.solution.isPalindrome(123454321))
    
    def test_large_non_palindrome(self):
        # Caso donde el número grande no es un palíndromo
        self.assertFalse(self.solution.isPalindrome(123456789))
    
    def test_zero(self):
        # Cero es un palíndromo
        self.assertTrue(self.solution.isPalindrome(0))

# Para ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
