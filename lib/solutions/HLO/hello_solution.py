

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """Return "Hello, World!"
    >>> hello("")
    'Hello, World!'
    """
    return "Hello, World!"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
