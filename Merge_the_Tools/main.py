from collections import OrderedDict


class OrderedSet(OrderedDict):
    """
    OrderedSet is a class that has the properties of
    both a set and a list. The elements inside an
    OrderedSet are unique, and their order is preserved
    """

    def add(self, element):
        """Add an element to the set"""
        self[element] = None


def merge_the_tools(string: str, k: int) -> None:
    """
    Split the string into substrings of length k, remove
    duplicates in each one, and print the resulting substrings.
    """
    num_substrings = len(string) // k
    for i in range(num_substrings):
        u = OrderedSet()
        t = string[k * i:k * (i + 1)]
        _ = [u.add(char) for char in t]

        print("".join(list(u.keys())))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
