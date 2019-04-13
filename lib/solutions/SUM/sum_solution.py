# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """Returns a + b where both are integers

    >>> compute(5, 10)
    10

    """
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
