

class Ingredient:

    def __init__(self, name='', vegetarian=False, fish=False, dairy=False, healthy=None, associated_cuisine=[], associated_prep=''):
        self.name = name
        self.vegetarian = vegetarian
        self.fish = fish
        self.dairy = dairy
        self.healthy = healthy
        self.associated_cuisine = associated_cuisine
        self.associated_prep = associated_prep

    def __str__(self):
        return str(self.name + '\nVegetarian? ' + str(self.vegetarian) + '\nFish? ' + str(self.fish) + '\nDairy? ' +
        str(self.dairy)  + '\nHealthy? ' + str(self.healthy) + ')\nAssociated Cuisine(s) : ' +
        str(self.associated_cuisine) + '\nAssociated Prep : ' + self.associated_prep)
