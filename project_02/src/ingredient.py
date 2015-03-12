

class Ingredient:
    def ingredient_from_recipie(self, name, qty, measure, prep, prep_description, description):
        self.name = name
        self.qty = qty
        self.measure = measure
        self.prep = prep
        self.prep_description = prep_description
        self.description = description

    def __init__(self, name='', diet=[], healthy=[], associated_cuisine=[]):
        self.name = name
        self.diet = diet
        self.healthy = healthy
        self.associated_cuisine = associated_cuisine
        self.qty = 0
        self.measure = ""
        self.prep = ""
        self.prep_description = ""
        self.description = []

    def isCuisine(self, cuisine_check):
        if cuisine_check.lower() in self.associated_cuisine:
            return True
        else:
            return False

    def isDiet(self, diet_check):
        if diet_check.lower() in self.diet:
            return True
        else:
            return False

    def isHealthy(self, health_check):
        if health_check.lower() in self.healthy:
            return True
        else:
            return False
