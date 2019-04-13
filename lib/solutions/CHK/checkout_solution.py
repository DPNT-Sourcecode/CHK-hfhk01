from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    >>> checkout("BEBEEE")
    160
    >>> checkout("ABCDEABCDE")
    280
    >>> checkout("ABCDECBAABCABBAAAEEAA")
    665
    >>> checkout("EE")
    80
    >>> checkout("-AA")
    -1
    >>> checkout("BB")
    45
    >>> checkout("B")
    30
    >>> checkout("BBB")
    75
    >>> checkout("A")
    50
    >>> checkout("AAAAA")
    200
    >>> checkout("AAAAAAAA")
    330
    >>> checkout("AAAAAAAAA")
    380
    >>> checkout("EEB")
    80
    """
    skuCounter = Counter(skus)
    price = 0
    free_bs = 0

    for c in skuCounter:
        if c not in "ABCDEF": return -1

    # Check the Fs
    

    # Check the Es
    price += skuCounter["E"] * 40
    free_bs = skuCounter["E"] // 2

    # Check the Ds
    price += skuCounter["D"]*15

    # Check the Cs
    price += skuCounter["C"]*20

    # Check the Bs
    b_count = skuCounter["B"] - free_bs
    if not b_count <= 0:
        remainder = b_count % 2
        price += 30 * remainder
        price += 45 * ((b_count - remainder) / 2)

    # Check the As
    a_count = skuCounter["A"]
    for count in range(a_count):
        if a_count >= 5:
            price += 200
            a_count -= 5
        elif a_count >= 3:
            price += 130
            a_count -= 3
        else:
            price += a_count * 50
            break
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



