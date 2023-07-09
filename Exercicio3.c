#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAXSIZE 2500

int n;
int v[MAXSIZE];
int w[MAXSIZE];
int dp[MAXSIZE][MAXSIZE];

int max(int a, int b) {
    return a > b ? a : b;
}

int solve(int u, int p) {
    if (u == n || p == 0)
        return 0;
    
    if (p < 0)
        return INT_MIN;

    if (dp[u][p] == -1)
        dp[u][p] = max(solve(u + 1, p), v[u] + solve(u, p - w[u]));

    return dp[u][p];
}

int main(int argc, char **argv) {
    int i, m;

   while (scanf("%d %d", &n, &m) != EOF) {
    i = 0;
    while (i < n) {
        scanf("%d %d", &w[i], &v[i]);
        i++;
    }

    memset(dp, -1, sizeof(dp));
    printf("%d\n", solve(0, m));
    }

    return 0;
}
