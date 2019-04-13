from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
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
    for skuKey in skuCounter:
        # If we do E first it makes calculating free Bs easier
        if skuKey == "E":
            price += skuCounter[skuKey]*40
            if skuCounter["E"] >= 2 and "E" in skuCounter:
                new_b_count = skuCounter["B"] - skuCounter["E"] // 2
                # Can't have less than 0 Bs
                if new_b_count >= 0:
                    free_bs = new_b_count
                else:
                    free_bs = 0
        elif skuKey == "D":
            price += skuCounter[skuKey]*15
        elif skuKey == "C":
            price += skuCounter[skuKey]*20
        elif skuKey == "B":
            b_count = skuCounter[skuKey] - free_bs
            price(b_count)
            if b_count <= 0:
                break
            remainder = b_count % 2
            price += 30 * remainder
            price += 45 * ((b_count - remainder) / 2)
        elif skuKey == "A":
            a_count = skuCounter[skuKey]
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
        else:
            return -1
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()






