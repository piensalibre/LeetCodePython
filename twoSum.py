from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        if len(nums) == 1:
            return []
        for indice, valor in enumerate(nums):
            resta = target - valor
            if resta in indices:
                return [indices[resta],indice]
            indices[valor] = indice
        return []