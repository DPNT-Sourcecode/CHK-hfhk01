from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    >>> checkout("BB")
    45
    >>> checkout("B")
    30
    >>> checkout("BBB")
    75
    >>> checkout("A")
    50
    >>> checkout("AAAA")
    180
    """
    skuCounter = Counter(skus)
    price = 0
    for item in skuCounter:
        if item not in ["A", "B", "C", "D"]:
            return -1
    for skuKey in skuCounter:
        if skuKey == "D":
            price += skuCounter[skuKey]*15
        elif skuKey == "C":
            price += skuCounter[skuKey]*20
        elif skuKey == "B":
            remainder = skuCounter[skuKey] % 2
            price += 30 * remainder
            price += 45 * ((skuCounter[skuKey] - remainder) / 2)
        elif skuKey == "A":
            remainder = skuCounter[skuKey] % 3
            price += 50 * remainder
            price += 130 * ((skuCounter[skuKey] - remainder) / 3)
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


