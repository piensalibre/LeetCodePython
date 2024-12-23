from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefijo = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefijo):
                prefijo = prefijo[:-1]
                if not prefijo:
                    return ""
        return prefijo