## Regular Item
class RegularItem:

    def __init__(self, item):
        self.item = item
    
    # Update sell_in value and quality value
    def update(self):
        self.update_sell_in()
        self.update_quality()

    # Update the sell_in value
    def update_sell_in(self):
        # Decreases with 1 daily
        self.item.sell_in -= 1

    # Update the quality value
    def update_quality(self):

        # Calculate the change in quality and add to the item property
        self.item.quality += self.calculate_quality_change()

        # Make sure we stay between 0 and 50
        self.item.quality = self.adjust_for_boundaries()

    # Calculate the quality change
    def calculate_quality_change(self):
        # Decreases by 1 or 2, depending on the sell_in
        return -1 if self.item.sell_in >= 0 else -2
    
    def adjust_for_boundaries(self):
        # Between 0 and 50
        return max(0, min(50, self.item.quality))

## Good Wine
class GoodWine(RegularItem):

    # Increase in quality instead of decrease
    def calculate_quality_change(self):
        return 1 if self.item.sell_in >= 0 else 2

## Legendary    
class Legendary(RegularItem):

    # Sell_in and quality do not change
    def update(self):
        pass

# Backstage Pass
class BackstagePass(RegularItem):

    def update_quality(self):
        # Special case: sell_in less than 0 equals 0 quality
        if self.item.sell_in < 0:
            self.item.quality = 0
        else:
            super().update_quality()

    def calculate_quality_change(self):
        # Special increases in quality
        if self.item.sell_in <= 5:
            return 3
        elif self.item.sell_in <= 10:
            return 2
        else:
            return 1
        
# Smelly Items
class SmellyItem(RegularItem):

    def calculate_quality_change(self):
        # Quality decreases twice as fast
        return -2 if self.item.sell_in >= 0 else -4
