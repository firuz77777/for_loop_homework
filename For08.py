def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    i = 1
    a = 0
    while i < N:
        a = a + 1 / N
    i += 1
    return float(a)
print(main(2))