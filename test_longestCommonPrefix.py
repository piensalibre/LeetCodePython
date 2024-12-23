import unittest
from typing import List
from longestCommonPrefix import LongestCommonPrefix


# Clase de pruebas
class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = LongestCommonPrefix()

    def test_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flor", "florida", "flota"]), "flo")

    def test_no_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["perro", "gato", "ratón"]), "")

    def test_empty_list(self):
        self.assertEqual(self.solution.longestCommonPrefix([]), "")

    def test_single_word(self):
        self.assertEqual(self.solution.longestCommonPrefix(["sol"]), "sol")

    def test_identical_words(self):
        self.assertEqual(self.solution.longestCommonPrefix(["casa", "casa", "casa"]), "casa")

    def test_one_empty_string(self):
        self.assertEqual(self.solution.longestCommonPrefix(["", "casa", "casona"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["", "", ""]), "")

    def test_partial_match(self):
        self.assertEqual(self.solution.longestCommonPrefix(["inter", "internacional", "internet"]), "inter")

    def test_prefix_is_a_whole_word(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abc", "abcd", "abcdef"]), "abc")

    def test_case_sensitivity(self):
        self.assertEqual(self.solution.longestCommonPrefix(["Casa", "casa"]), "")

# Ejecución de las pruebas
if __name__ == "__main__":
    unittest.main()
