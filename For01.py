def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returs:
        nlist: return  answer
    """
    
    sum = []
    for i in range(n):
        sum.append(i)
    return sum 
print(main(9))