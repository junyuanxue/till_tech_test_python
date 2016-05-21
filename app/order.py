class Order(object):

    def __init__(self, menu):
        self._items = {}
        self._menu = menu
        self._prices = []
        self._DEFAULT_TAX_RATE = 0.0864

    def add_item(self, item, quantity = 1):
        self._items[item] = quantity

    def sum_items(self):
        self._calcaulate_each_item()
        return sum(self._prices)

    def calculate_tax(self):
        tax = self.sum_items() * self._DEFAULT_TAX_RATE
        return round(tax, 2)

    def total(self):
        total = self.sum_items() * (1 + self._DEFAULT_TAX_RATE)
        return round(total, 2)

    def _calcaulate_each_item(self):
        for item, quantity in self._items.items():
            self._prices.append(self._menu[item] * quantity)