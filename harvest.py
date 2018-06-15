############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yw = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print("{} pairs with: ".format(melon_type.name))
        for pairing in melon_type.pairings:
            print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code = {}
    for melon_type in melon_types:
        melon_code[melon_type.code] = melon_type

    return melon_code


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    def __init__(self, melon_number, name, shape_rating, color_rating, field, harvester):
        self.name = name
        self.melon_number = melon_number
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, field):
        """method should return 'True' or 'False' based on sellablity."""
        if shape_rating > 5 and color_rating > 5 and field != 3:
            self.sellability = True
        else:
            self.sellability = False
          

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Need to create a link between MelonTypes (dictionary) and make melons

    all_melons = []
    
    melon_1 = Melon('1', 'yw', 8, 7, 2, 'sheila')
    all_melons.append(melon_1)

    melon_2 = Melon('2', 'yw', 3, 4, 2, 'sheila')
    all_melons.append(melon_2)

    melon_3 = Melon('3', 'yw', 9, 8, 3, 'sheila')
    all_melons.append(melon_3)

    melon_4 = Melon('4', 'cas', 10, 6, 35, 'sheila')
    all_melons.append(melon_4)

    melon_5 = Melon('5', 'cren', 8, 9, 35, 'michael')
    all_melons.append(melon_5)

    melon_6 = Melon('6', 'cren', 8, 2, 35, 'michael')
    all_melons.append(melon_6)

    melon_7 = Melon('7', 'cren', 2, 3, 4, 'michael')
    all_melons.append(melon_7)

    melon_8 = Melon('8', 'musk', 6, 7, 4, 'michael')
    all_melons.append(melon_8)

    melon_9 = Melon('9', 'yw', 7, 10, 3, 'sheila')
    all_melons.append(melon_9)

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



