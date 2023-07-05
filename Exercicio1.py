from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        prefix_ones = [0] * (n + 1)
        suffix_ones = [0] * (n + 1)

        # Calcular o número de uns consecutivos no prefixo
        for i in range(1, n + 1):
            if nums[i - 1] == 1:
                prefix_ones[i] = prefix_ones[i - 1] + 1

        # Calcular o número de uns consecutivos no sufixo
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                suffix_ones[i] = suffix_ones[i + 1] + 1

        # Encontrar a resposta máxima após remover um elemento
        for i in range(n):
            max_len = max(max_len, prefix_ones[i] + suffix_ones[i + 1])

        return max_len
