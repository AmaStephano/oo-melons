"""This file should have our order classes in it."""

import random
import datetime

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        
        if qty > 100:
            raise TooManyMelonsError

        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_base_price(self):
        current_time = datetime.datetime.now().time()
        hour = current_time.hour
        base = random.randint(5,9)

        if day_of_week < 5 and hour > 7 and hour < 11:
            base += 4

        return base


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species.lower() == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08)
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty, 'international', 0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, 'government', 0)

    def mark_inspection(self, passed):
        self.passed_inspection = passed

        return self.passed_inspection

# More like a mixin, but you don't have to name it as a mixin. 
class TooManyMelonsError(ValueError):
    def __init__(self):
        super(TooManyMelonsError,self).__init__("No more than 100 melons")


