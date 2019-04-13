from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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
                price += (skuCounter[skuKey]-1/2) * 130
                price += 50
            





