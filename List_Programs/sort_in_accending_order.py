class SortByOrder:
    def __init__(self):
        pass

    def sort_the_list(self):
        """
        sorting the list
        containing tuple elements
        """
        given_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        return sorted(given_list, key=lambda element: element[1])


if __name__ == "__main__":
    sortby = SortByOrder()
    print(sortby.sort_the_list())
