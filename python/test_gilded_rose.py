import pytest

from gilded_rose import GildedRose, Item


def brie_quality_increase(quality: int) -> int:
    return quality + 1


def sell_in_decrease(sell_in: int) -> int:
    return sell_in - 1


def default_quality_decrease(quality: int) -> int:
    return quality - 1


class TestDefault:
    """
    Test basic functionality: decrease sell_in by 1 and decrease quality by one
    GIVEN: GildedRose with one Item of type default
    WHEN: call update_quality method
    THEN: quality should be one less and sell_in should be one less
    """
    quality = 10
    sell_in = 20
    name = 'default'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_default(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_decrease(self, create_default):
        assert self.items[0].quality == default_quality_decrease(self.quality)

    def test_sell_in_decrease(self, create_default):
        assert self.items[0].sell_in == sell_in_decrease(self.sell_in)


def test_default_quality_2_down():
    """
    Test that quality goes down by 2 when sell_in date has gotten to 0
    GIVEN: GildedRose with one Item of type default
    WHEN: call update_quality method
    THEN: quality should be two less
    """
    quality = 10
    sell_in = 0
    name = 'default'

    items = [Item(name, sell_in, quality)]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    assert items[0].quality == quality - 2


def test_quality_never_negative():
    """
    Test that quality does not become negative
    GIVEN: GildedRose with one Item of type default - quality at 0
    WHEN: call update_quality method
    THEN: quality should stay at 0
    """
    # quality never negative
    quality = 0
    sell_in = 10
    name = 'default'

    items = [Item(name, sell_in, quality)]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    assert items[0].quality == 0


class TestAgedBrieNormal:
    """
    Test basic functionality of `aged brie`: quality increases by 1
    GIVEN: GildedRose with one Item of type `aged brie`
    WHEN: call update_quality method
    THEN: quality should be one more and sell_in should be one less
    """
    # aged brie - quality goes up by one
    quality = 10
    sell_in = 20
    name = 'aged brie'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_aged_brie(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_aged_brie):
        assert self.items[0].quality == brie_quality_increase(self.quality)

    def test_sell_in_decrease(self, create_aged_brie):
        assert self.items[0].sell_in == sell_in_decrease(self.sell_in)


class TestAgedBrieQuality50:
    """
    Test basic functionality: decrease sell_in by 1 and decrease quality by one
    GIVEN: GildedRose with one Item of type default
    WHEN: call update_quality method
    THEN: quality should be one less and sell_in should be one less
    """
    # aged brie - never over 50
    quality = 50
    sell_in = 20
    name = 'aged brie'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_aged_brie(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_aged_brie):
        assert self.items[0].quality == self.quality

    def test_sell_in_decrease(self, create_aged_brie):
        assert self.items[0].sell_in == sell_in_decrease(self.sell_in)


class TestSulfuras:
    """
    Test basic functionality: decrease sell_in by 1 and decrease quality by one
    GIVEN: GildedRose with one Item of type default
    WHEN: call update_quality method
    THEN: quality should be one less and sell_in should be one less
    """
    # sulfuras - always 80 quality and age doesn't decrease
    quality = 10
    sell_in = 20
    name = 'sulfuras'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_sulfuras(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_name(self, create_sulfuras):
        assert self.items[0].name == self.name

    def test_quality(self, create_sulfuras):
        assert self.items[0].quality == self.quality

    def test_sell_in(self, create_sulfuras):
        assert self.items[0].sell_in == self.sell_in


class TestBackstageNormal:
    """
    Test backstage normal
    GIVEN: GildedRose with one Item of type `backstage passes`
    WHEN: call update_quality method
    THEN: quality should be one more and sell_in should be one less
    """
    # backstage passes Normal
    quality = 10
    sell_in = 20
    name = 'backstage passes'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_backstage(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_backstage):
        assert self.items[0].quality == self.quality + 1

    def test_sell_in_decrease(self, create_backstage):
        assert self.items[0].sell_in == self.sell_in - 1


class TestBackstageQuality50:
    """
    Test backstage quality not greater than 50
    GIVEN: GildedRose with one Item of type `backstage passes` with quality at 50
    WHEN: call update_quality method
    THEN: quality should stay at 50 and sell_in should be one less
    """
    # backstage passes Normal
    quality = 50
    sell_in = 20
    name = 'backstage passes'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_backstage(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_backstage):
        assert self.items[0].quality == 50

    def test_sell_in_decrease(self, create_backstage):
        assert self.items[0].sell_in == self.sell_in - 1


class TestBackstage10Day:
    """
    Test backstage: quality increase when sell in less than 10
    GIVEN: GildedRose with one Item of type backstage with sell_in at 10
    WHEN: call update_quality method
    THEN: quality should be two more and sell_in should be one less
    """
    # backstage passes - 10 days - up 2 quality
    quality = 20
    sell_in = 10
    name = 'backstage passes'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_backstage(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_backstage):
        assert self.items[0].quality == self.quality + 2

    def test_sell_in_decrease(self, create_backstage):
        assert self.items[0].sell_in == self.sell_in - 1


class TestBackstage5Day:
    """
    Test backstage: quality increase when sell in less than 5
    GIVEN: GildedRose with one Item of type backstage with sell_in at 5
    WHEN: call update_quality method
    THEN: quality should be three more and sell_in should be one less
    """
    # backstage passes - 5 days - up 3 quality
    quality = 20
    sell_in = 5
    name = 'backstage passes'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_backstage(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_backstage):
        assert self.items[0].quality == self.quality + 3

    def test_sell_in_decrease(self, create_backstage):
        assert self.items[0].sell_in == self.sell_in - 1


class TestBackstage0Day:
    """
    Test backstage: quality goes to zero when sell_in has less than or equal to 0
    GIVEN: GildedRose with one Item of type backstage with sell_in at 0
    WHEN: call update_quality method
    THEN: quality should be 0 and sell_in should be one less
    """
    # backstage passes - 0 days - quality == 0
    quality = 20
    sell_in = 0
    name = 'backstage passes'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_backstage(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_increase(self, create_backstage):
        assert self.items[0].quality == 0

    def test_sell_in_decrease(self, create_backstage):
        assert self.items[0].sell_in == self.sell_in - 1


class TestConjured:
    """
    Test conjured: decreases by twice the normal rate
    GIVEN: GildedRose with one Item of type `conjured`
    WHEN: call update_quality method
    THEN: quality should be two less and sell_in should be one less
    """
    # conjured - quality down 2
    quality = 10
    sell_in = 20
    name = 'conjured'

    items = [Item(name, sell_in, quality)]

    @pytest.fixture(scope='class')
    def create_conjured(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_decrease(self, create_conjured):
        assert self.items[0].quality == self.quality - 2

    def test_sell_in_decrease(self, create_conjured):
        assert self.items[0].sell_in == self.sell_in - 1


def test_conjured_quality_4_down():
    """
    Test conjured: decreases by twice the normal rate - sell_in has reached 0
    GIVEN: GildedRose with one Item of type `conjured` with sell_in at 0
    WHEN: call update_quality method
    THEN: quality should be four less and sell_in should be one less
    """
    quality = 10
    sell_in = 0
    name = 'conjured'

    items = [Item(name, sell_in, quality)]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    assert items[0].quality == quality - 4


class TestTwoItems:
    """
    Test GildedRose handles more than one `Item` and that type is case-insensitive
    GIVEN: GildedRose with one Item of type default
    WHEN: call update_quality method
    THEN: quality should be one less and sell_in should be one less
    """
    brie_quality = 10
    brie_sell_in = 20
    brie_name = 'Aged Brie'

    default_quality = 30
    default_sell_in = 40
    default_name = 'Default'

    items = [Item(brie_name, brie_sell_in, brie_quality),
             Item(default_name, default_sell_in, default_quality),
             ]

    @pytest.fixture(scope='class')
    def create_rose(self):
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_quality_brie(self, create_rose):
        assert self.items[0].quality == brie_quality_increase(self.brie_quality)

    def test_sell_in_brie(self, create_rose):
        assert self.items[0].sell_in == sell_in_decrease(self.brie_sell_in)

    def test_quality_default(self, create_rose):
        assert self.items[1].quality == default_quality_decrease(self.default_quality)

    def test_sell_in_default(self, create_rose):
        assert self.items[1].sell_in == sell_in_decrease(self.default_sell_in)
