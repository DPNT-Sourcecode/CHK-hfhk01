

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """Return "Hello, World!"
    >>> hello("Rowan")
    'Hello, Rowan!'
    """
    return "Hello, {}!".format(friend_name)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
