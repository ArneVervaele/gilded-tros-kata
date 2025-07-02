# -*- coding: utf-8 -*-

from item_factory import assign_item_to_class

class GildedTros(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updated_item = assign_item_to_class(item)
            updated_item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
