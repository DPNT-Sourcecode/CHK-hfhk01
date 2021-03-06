from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skuCounter = Counter(skus)
    
    # Performs side effects on the skuCounter :(
    price, skuCounter = do_buy_any_deal(skuCounter.copy())

    for c in skuCounter:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": return -1

    # Check the Zs
    # New offer
    price += skuCounter["Z"] * 21

    # Check the Ys
    # New offer
    price += skuCounter["Y"] * 20

    # Check the Xs
    # New offer
    price += skuCounter["X"] * 17

    # Check the Ws
    price += skuCounter["W"] * 20

    # Check the Vs
    price += calculate_double_money_off_deal(50, skuCounter["V"], 3, 130, 2, 90)

    # Check the Us
    price += calculate_get_one_free_deal(40, skuCounter["U"], 4)

    # Check the Ts
    # New offer
    price += skuCounter["T"] * 20

    # Check the Ss
    # New offer
    price += skuCounter["S"] * 20

    # Check the Rs
    price += skuCounter["R"] * 50
    free_qs = skuCounter["R"] // 3

    # Check the Qs
    if skuCounter["Q"] - free_qs > 0:
        price += calculate_single_money_off_deal(30, skuCounter["Q"] - free_qs, 3, 80)
    
    # Check the Ps
    price += calculate_single_money_off_deal(50, skuCounter["P"], 5, 200)

    # Check the Os
    price += skuCounter["O"] * 10

    # Check the Ns
    price += skuCounter["N"] * 40
    free_Ms = skuCounter["N"] // 3

    # Check the Ms
    if skuCounter["M"]-free_Ms > 0:
        price += (skuCounter["M"]-free_Ms) * 15
    

    # Check the Ls
    price += skuCounter["L"] * 90

    # Check the Ks
    price += calculate_single_money_off_deal(70, skuCounter["K"], 2, 120)

    # Check the Js
    price += skuCounter["J"] * 60

    # Check the Is
    price += skuCounter["I"] * 35

    # Check the Hs
    price += calculate_double_money_off_deal(10, skuCounter["H"], 10, 80, 5, 45)

    # Check the Gs
    price += skuCounter["G"] * 20

    # Check the Fs
    price += calculate_get_one_free_deal(10, skuCounter["F"], 3) 

    # Check the Es
    price += skuCounter["E"] * 40
    free_bs = skuCounter["E"] // 2

    # Check the Ds
    price += skuCounter["D"]*15

    # Check the Cs
    price += skuCounter["C"]*20

    # Check the Bs
    if skuCounter["B"]-free_bs > 0:
        price += calculate_single_money_off_deal(30, skuCounter["B"]-free_bs, 2, 45)

    # Check the As
    price += calculate_double_money_off_deal(50, skuCounter["A"], 5, 200, 3, 130)

    return int(price)


def reduce_counts(skuCounter, sku, count):
    while skuCounter[sku] > 0 and count > 0:
        skuCounter[sku] -= 1
        count -= 1
    return count


def do_buy_any_deal(skuCounter: Counter):
    """
    >>> do_buy_any_deal(Counter({"X":3}))
    (45, Counter({'X': 0}))
    >>> do_buy_any_deal(Counter({"X":3, "T":2}))
    (45, Counter({'X': 2, 'T': 0}))
    >>> do_buy_any_deal(Counter({"X":1, "T":1}))
    (0, Counter({'X': 1, 'T': 1}))
    """
    deal_skus = "ZYSTX" # In descending order of price
    count = 0
    for c in deal_skus:
        count += skuCounter[c]
    value = (count // 3) * 45

    # Important to use floor division to remove remainders
    amount_to_remove = (count // 3) * 3
    for sku in deal_skus:
        amount_to_remove = reduce_counts(skuCounter, sku, amount_to_remove)
    return value, skuCounter


def calculate_get_one_free_deal(item_price, item_count, free_point):
    free = item_count // free_point
    count_minus_free = item_count - free
    price = count_minus_free * item_price
    return price


def calculate_double_money_off_deal(item_price, item_count, 
    deal_count1, deal_price1, deal_count2, deal_price2):
    price = 0
    if not item_count <= 0:
        while item_count > 0:
            if item_count >= deal_count1:
                price += deal_price1
                item_count -= deal_count1
            elif item_count >= deal_count2:
                price += deal_price2
                item_count -= deal_count2
            else:
                price += item_count * item_price
                break
    return int(price)


def calculate_single_money_off_deal(item_price, item_count, deal_count, deal_price):
    price = 0
    if not item_count <= 0:
        while item_count > 0:
            if item_count >= deal_count:
                price += deal_price
                item_count -= deal_count
            else:
                price += item_count * item_price
                break
    return int(price)


def test_checkout(skus):
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
    >>> checkout("BBB")
    75
    >>> checkout("AAAAA")
    200
    >>> checkout("AAAAAAAA")
    330
    >>> checkout("AAAAAAAAA")
    380
    >>> checkout("EEB")
    80
    >>> checkout("FFFF")
    30
    >>> checkout("UUUU")
    120
    >>> checkout("VV")
    90
    >>> checkout("VVV")
    130
    >>> checkout("VVVV")
    180
    >>> checkout("VVVVV")
    220
    >>> checkout("RRRQ")
    150
    >>> checkout("NNNNNN")
    240
    >>> checkout("NNNM")
    120
    >>> checkout("HHHHHH")
    55
    >>> checkout("S")
    20
    >>> checkout("ABCDEFGHIJKLMNOPQRSTUVW")
    795
    >>> checkout("SSSZ")
    65
    """
    checkout(skus)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

