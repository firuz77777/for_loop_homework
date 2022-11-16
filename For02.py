def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a = ''
    i = 0
    for i in range(n):
        a = a + str(i)
    return a
print(main(9))