from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        num_crimes = len(group)

        # Cria uma matriz dp para armazenar a contagem de esquemas
        # dp[i][j][k] representa a contagem de esquemas com j membros e pelo menos k lucro
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(num_crimes + 1)]

        # Inicializa o caso base dp[0][0][0] como 1, pois não realizar nenhum crime também é um esquema válido
        dp[0][0][0] = 1

        for i in range(1, num_crimes + 1):
            curr_members = group[i - 1]
            curr_profit = profit[i - 1]

            for j in range(n + 1):
                for k in range(minProfit + 1):
                    # Caso 1: Não realizar o crime atual
                    dp[i][j][k] = dp[i - 1][j][k]

                    # Caso 2: Realizar o crime atual
                    if j >= curr_members:
                        prev_members = j - curr_members
                        prev_profit = max(0, k - curr_profit)
                        dp[i][j][k] += dp[i - 1][prev_members][prev_profit]

                    dp[i][j][k] %= MOD

        total_schemes = sum(dp[num_crimes][j][minProfit] for j in range(n + 1))
        return total_schemes % MOD
