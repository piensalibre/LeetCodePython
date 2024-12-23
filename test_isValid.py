import unittest

from isValid import IsValid

class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.validator = IsValid()

    def test_empty_string(self):
        self.assertTrue(self.validator.isValid(""), "Cadena vacía debería ser válida.")

    def test_valid_parentheses(self):
        self.assertTrue(self.validator.isValid("()"), "'()' debería ser válido.")
        self.assertTrue(self.validator.isValid("()[]{}"), "'()[]{}' debería ser válido.")
        self.assertTrue(self.validator.isValid("{[()]}"), "'{[()]}' debería ser válido.")

    def test_invalid_parentheses(self):
        self.assertFalse(self.validator.isValid("(]"), "'(]' debería ser inválido.")
        self.assertFalse(self.validator.isValid("([)]"), "'([)]' debería ser inválido.")
        self.assertFalse(self.validator.isValid("("), "'(' debería ser inválido.")
        self.assertFalse(self.validator.isValid("}"), "'}' debería ser inválido.")

    
if __name__ == "__main__":
    unittest.main()
