class IsPalindrome:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        cadena = str(x)
        return cadena == cadena[::-1]