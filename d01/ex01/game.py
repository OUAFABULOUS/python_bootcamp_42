class GotCharacter:
    def	__init__(self, first_name,is_alive=True):
        if (type(first_name) is not str):
            raise Exception  ("first_name should be a string")
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """
    A class representing the Stark family. Or when bad things happen to good people.
    """
    def	__init__(self, first_name, is_alive=True, family_name="", house_words="Winter is Coming"):
        if (type(house_words) is not str):
            raise Exception ("House words should be a str")
        super().__init__(first_name, is_alive)
        self.house_words=house_words
        self.family_name = self.__class__.__name__

    def	print_house_words(self):
        print(self.house_words)

    def	die(self):
        self.is_alive = False
