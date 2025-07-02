from item_classes import RegularItem, GoodWine, Legendary, BackstagePass, SmellyItem

# Assign the given item to the correct class based on the item name
def assign_item_to_class(item):

    if item.name == "Good Wine":
        return GoodWine(item)
    if item.name == "B-DAWG Keychain":
        return Legendary(item)
    if "Backstage passes" in item.name:
        return BackstagePass(item)
    if item.name in ["Duplicate Code", "Long Methods", "Ugly Variable Names"]:
        return SmellyItem(item)

    return RegularItem(item)
