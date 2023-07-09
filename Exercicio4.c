int helper(int ind, int arr[], int size, int k, int dp[]) {
    if (ind == size)
        return 0;
    
    if (dp[ind] != -1)
        return dp[ind];

    int maxi = INT_MIN;
    int maxAns = INT_MIN;
    int len = 0;

    for (int i = ind; i < (ind + k < size ? ind + k : size); i++) {
        len++;
        if (arr[i] > maxi)
            maxi = arr[i];

        int sum = maxi * len + helper(i + 1, arr, size, k, dp);
        if (sum > maxAns)
            maxAns = sum;
    }

    return dp[ind] = maxAns;
}

int maxSumAfterPartitioning(int arr[], int size, int k) {
    int dp[size];
    for (int i = 0; i < size; i++)
        dp[i] = -1;

    return helper(0, arr, size, k, dp);
}