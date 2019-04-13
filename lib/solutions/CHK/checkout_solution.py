from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
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
    >>> checkout("EEB")
    80
    """
    skuCounter = Counter(skus)
    price = 0
    for item in skuCounter:
        if item not in ["A", "B", "C", "D", "E"]:
            return -1
    for skuKey in skuCounter:
        if skuKey == "E":
            price += skuCounter[skuKey]*40
            new_b_count = skuCounter["B"] - skuCounter["E"] // 2
            # Can't have -1 Bs
            if new_b_count >= 0:
                skuCounter["B"] = new_b_count
            else:
                skuCounter["B"] = 0
        if skuKey == "D":
            price += skuCounter[skuKey]*15
        elif skuKey == "C":
            price += skuCounter[skuKey]*20
        elif skuKey == "B":
            remainder = skuCounter[skuKey] % 2
            price += 30 * remainder
            price += 45 * ((skuCounter[skuKey] - remainder) / 2)
        elif skuKey == "A":
            a_count = skuCounter[skuKey]
            for count in range(a_count):
                if a_count >= 5:
                    price += 200
                    a_count -= 5
                elif a_count >= 3:
                    price += 130
                    a_count - 3
                else:
                    price += a_count * 50
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
