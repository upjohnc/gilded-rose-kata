from typing import List


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    @staticmethod
    def aged_brie_quality(item_: Item) -> None:
        """
        Brie quality
        - quality goes up
        - quality never goes above 50
        """
        if item_.quality < 50:
            item_.quality += 1

    @staticmethod
    def sulfuras_quality(item_: Item) -> None:
        """
        Sulfuras quality
        - quality never decreases
        """
        pass

    @staticmethod
    def sulfuras_sell_in(item_: Item) -> None:
        """
        Sulfuras quality
        - sell_in never decreases
        """
        pass

    @staticmethod
    def backstage_quality(item_: Item) -> None:
        """
        Backstage passes quality
        - quality goes up by 1
        - quality goes up by 2 when less than 10 days of sell_in
        - quality goes up by 3 when less than 5 days of sell_in
        - quality goes to 0 when sell_in is less than or equal to 0
        - quality cannot go above 50
        """
        if item_.quality >= 50:
            return
        if item_.sell_in <= 0:
            item_.quality = 0
        elif item_.sell_in <= 5:
            item_.quality += 3
        elif item_.sell_in <= 10:
            item_.quality += 2
        else:
            item_.quality += 1

    @staticmethod
    def conjured_quality(item_: Item) -> None:
        """
        Conjured quality
        - quality decreases twice as fast as the default
            - decreases by 2 when sell_in is greater than 0
            - decreases by 4 when sell_in is less than or equal to 0
        """
        if item_.quality > 0:
            quality_decrease = 2
            if item_.sell_in <= 0:
                quality_decrease = 4
            item_.quality -= quality_decrease

    @staticmethod
    def default_quality_method(item_: Item) -> None:
        """
        Default quality
        - decreases by 1
        - quality cannot by negative
        """
        if item_.quality > 0:
            quality_decrease = 1
            if item_.sell_in <= 0:
                quality_decrease = 2
            item_.quality -= quality_decrease

    @staticmethod
    def default_sell_in_method(item_: Item) -> None:
        """
        Default sell_in
        - decreases by 1
        """
        item_.sell_in -= 1

    def update_quality(self) -> None:
        quality_update_methods = {'aged brie': self.aged_brie_quality,
                                  'sulfuras': self.sulfuras_quality,
                                  'backstage passes': self.backstage_quality,
                                  'conjured': self.conjured_quality,
                                  }
        sell_in_update_methods = {'sulfuras': self.sulfuras_sell_in, }
        for item in self.items:
            # based on the way the code was previously quality is updated and then sell_in adjusted
            update_quality = quality_update_methods.get(item.name.lower(), self.default_quality_method)
            _ = update_quality(item)  # noqa

            update_sell_in = sell_in_update_methods.get(item.name.lower(), self.default_sell_in_method)
            _ = update_sell_in(item)  # noqa
