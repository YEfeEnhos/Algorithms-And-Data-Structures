def count_partition(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partition(n-m, m) + count_partition (n, m-1)