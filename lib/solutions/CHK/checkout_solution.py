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
    >>> checkout("FFFFFF")
    40
    """
    skuCounter = Counter(skus)
    price = 0
    free_bs = 0

    for c in skuCounter:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": return -1

    # Check the Zs
    price += skuCounter["Z"] * 50

    # Check the Ys
    price += skuCounter["Y"] * 10

    # Check the Xs
    price += skuCounter["X"] * 90

    # Check the Ws
    price += skuCounter["W"] * 20

    # Check the Vs
    # Check the Us
    # Check the Ts
    price += skuCounter["T"] * 20

    # Check the Ss
    price += skuCounter["S"] * 30

    # Check the Rs
    # Check the Qs
    # Check the Ps
    # Check the Os
    price += skuCounter["O"] * 10

    # Check the Ns

    # Check the Ms
    price += skuCounter["M"] * 15

    # Check the Ls
    price += skuCounter["L"] * 90
    # Check the Ks

    # Check the Js
    price += skuCounter["J"] * 60

    # Check the Is
    price += skuCounter["I"] * 35

    # Check the Hs


    # Check the Gs
    price += skuCounter["G"] * 20

    # Check the Fs
    price += calculate_f(price, skuCounter["F"])
    

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

def calculate_deal(price, item_count, deal_num, deal_price):
    if not item_count <= 0:
        for count in range(a_count):
        if a_count >= deal_count:
            price += 200
            a_count -= 5
        elif a_count >= 3:
            price += 130
            a_count -= 3
        else:
            price += a_count * 50
            break
    return int(price)

def calculate_f(price, f_count):
    free_fs = f_count // 3
    f_count_minus_free = f_count - free_fs
    price += f_count_minus_free * 10
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()






