class AddKey:
    def __init(self):
        """
        defining a dictionary
        """
        self.dict_elements

    def add_key_to_dictionary(self):
        """
        adding a new key to the dictionary
        """
        self.dict_elements = {0: 10, 1: 20}
        self.dict_elements[2] = 30
        print("new dictionary elements :", self.dict_elements)


if __name__ == "__main__":
    addkey = AddKey()
    addkey.add_key_to_dictionary()
