"""Matrix algos
"""
from typing import List


def prefix_sum(mat: List[List[int]]):
    """Prefix sum;
    We use DP
    """
    n_rows = len(mat)
    n_cols = len(mat[0])
    dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            value = mat[row][col]
            left_row, left_col = row, col - 1
            up_row, up_col = row - 1, col
            diag_row, diag_col = row - 1, col - 1
            if (
                min(left_row, up_row) >= 0 and max(left_row, up_row) <= n_rows - 1
                and min(left_col, up_col) >= 0 and max(left_col, up_col) <= n_cols - 1
            ):
                value += dp[left_row][left_col] + dp[up_row][up_col] - dp[diag_row][diag_col]
            elif (
                0 <= left_row <= n_rows - 1
                and 0 <= left_col <= n_cols - 1
            ):
                value += dp[left_row][left_col]
            elif (
                0 <= up_row <= n_rows - 1
                and 0 <= up_col <= n_cols - 1
            ):
                value += dp[up_row][up_col]

            dp[row][col] = value

    print(dp)


if __name__ == "__main__":
    prefix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    prefix_sum([[10, 20, 30], [5, 10, 20], [2, 4, 6]])
