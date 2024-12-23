class IsValid:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        abiertos = []
        parejas = {'{':'}',"[":']','(':')'}
        for caracter in s:
            if caracter in parejas:
                abiertos.append(caracter)
            elif not abiertos or parejas[abiertos.pop()]!=caracter:
                return False
        return len(abiertos) ==0