def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returs:
        nlist: return  answer
    """
    
    a = []
    for i in range(n):
        a.append(i)
    return a 
print(main(9))