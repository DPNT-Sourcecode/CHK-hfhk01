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
    price += calculate_double_money_off_deal(50, skuCounter["V"], 3, 130, 2, 90)

    # Check the Us
    price += calculate_get_one_free_deal(40, skuCounter["U"], 3)
    # Check the Ts
    price += skuCounter["T"] * 20

    # Check the Ss
    price += skuCounter["S"] * 30

    # Check the Rs
    # Check the Qs
    price += calculate_single_money_off_deal(30, skuCounter["Q"], 3, 80)
    
    # Check the Ps
    price += calculate_single_money_off_deal(50, skuCounter["P"], 5, 200)

    # Check the Os
    price += skuCounter["O"] * 10

    # Check the Ns

    # Check the Ms
    price += skuCounter["M"] * 15

    # Check the Ls
    price += skuCounter["L"] * 90

    # Check the Ks
    price += calculate_single_money_off_deal(80, skuCounter["K"], 2, 150)

    # Check the Js
    price += skuCounter["J"] * 60

    # Check the Is
    price += skuCounter["I"] * 35

    # Check the Hs


    # Check the Gs
    price += skuCounter["G"] * 20

    # Check the Fs
    price += calculate_get_one_free_deal(10, skuCounter["F"], 3) #calculate_f(skuCounter["F"])
    

    # Check the Es
    price += skuCounter["E"] * 40
    free_bs = skuCounter["E"] // 2

    # Check the Ds
    price += skuCounter["D"]*15

    # Check the Cs
    price += skuCounter["C"]*20

    # Check the Bs
    price += calculate_single_money_off_deal(30, skuCounter["B"]-free_bs, 2, 45)

    # Check the As
    price += calculate_double_money_off_deal(50, skuCounter["A"], 5, 200, 3, 130)

    return int(price)

def calculate_get_one_free_deal(item_price, item_count, free_point):
    free = item_count // free_point
    count_minus_free = item_count - free
    price = count_minus_free * 10
    return int(price)

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

def calculate_f(f_count):
    price = 0
    free_fs = f_count // 3
    f_count_minus_free = f_count - free_fs
    price += f_count_minus_free * 10
    return int(price)

if __name__ == "__main__":
    import doctest
    doctest.testmod()






