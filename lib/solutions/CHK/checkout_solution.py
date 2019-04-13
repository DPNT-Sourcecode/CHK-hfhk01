from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skuCounter = Counter(skus)
    for item in skuCounter:
        if item not in ["A", "B", "C", "D"]:
            return -1
    for skuKey in skuCounter:
        if skuKey == "D":




