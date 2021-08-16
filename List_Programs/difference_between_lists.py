class Difference:
    def __init__(self):
        self.list1 = list1
        self.list2 = list2
        self.list_differcence = []

    def difference_of_two_list(self, list_differcence):
        """
        getting the difference
        between two lists
        """

        for elements in list1:
            if elements not in list2:
                list_differcence.append(elements)
        print("List difference :", list_differcence)


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 'python', '(2,"a")']
    list2 = [1, 2, "xy", 'dog', 6, 10]
    differ = Difference()
    differ.difference_of_two_list([])
