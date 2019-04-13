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
    120
    >>> checkout("A")
    50
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
            if skuCounter[skuKey] % 2 == 0:
                price += (skuCounter[skuKey]/2) * 45
            else:
                b_count = skuCounter[skuKey] -1 
                price += (b_count/2) * 45
                price += 30
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

