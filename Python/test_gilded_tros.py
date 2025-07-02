# -*- coding: utf-8 -*-
import unittest

from gilded_tros import Item, GildedTros


class GildedTrosTest(unittest.TestCase):

    # Regular Item
    def test_regular_item(self):
        items = [Item("Ring of Cleansening Code", 10, 20)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    # Regular Item expired
    def test_regular_item_expired(self):
        items = [Item("Ring of Cleansening Code", -1, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    # Good Wine
    def test_good_wine(self):
        items = [Item("Good Wine", 10, 20)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    # Good Wine expired
    def test_good_wine_expired(self):
        items = [Item("Good Wine", -1, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    # Good Wine
    def test_good_wine(self):
        items = [Item("Good Wine", 10, 20)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    # Good Wine expired
    def test_good_wine_expired(self):
        items = [Item("Good Wine", -1, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    # Legendary Item
    def test_legendary_item(self):
        items = [Item("B-DAWG Keychain", 10, 80)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # Backstage pass > 10
    def test_backstage_pass_20(self):
        items = [Item("Backstage passes for HAXX", 20, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(7, items[0].quality)

    # Backstage pass <= 10
    def test_backstage_pass_8(self):
        items = [Item("Backstage passes for HAXX", 8, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    # Backstage pass <= 5
    def test_backstage_pass_3(self):
        items = [Item("Backstage passes for HAXX", 3, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    # Backstage pass = 0
    def test_backstage_pass_0(self):
        items = [Item("Backstage passes for HAXX", 0, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Smelly items
    def test_smelly_item(self):
        items = [Item("Duplicate Code", 10, 20)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    # Smelly items expired
    def test_smelly_item_expired(self):
        items = [Item("Duplicate Code", -1, 6)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    # Negative quality not allowed
    def test_negative_quality(self):
        items = [Item("Ring of Cleansening Code", 10, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(0, items[0].quality)

    # Quality cannot be over 50
    def test_quality_over_50(self):
        items = [Item("Good Wine", 10, 50)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(50, items[0].quality)

    # Legendary item has quality 80
    def test_legendary_quality_80(self):
        items = [Item("B-DAWG Keychain", 10, 75)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(80, items[0].quality)

if __name__ == '__main__':
    unittest.main()
