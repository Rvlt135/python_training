from operator import attrgetter


class Flower:

    def __init__(self, name, color, time_live: int, price: int):
        self.name = name
        self.color = color
        self.time_live = time_live
        self.price = price


class Bouquet:
    def __init__(self):
        self.flowers = []

    def collect_flowers(self, *args):
        for it in args:
            self.flowers.append(it)

    def bouquet_price(self):
        price = sum([it.price for it in self.flowers])
        return print(price)

    def check_time_line(self):
        t_live = sum([it.time_live for it in self.flowers])
        result = t_live // len(self.flowers)
        return print(result)

    '''Не получилось реализовать сортировку нормально'''
    def sort_attribute(self, atr):
        return print(sorted(self.flowers, key=attrgetter(atr)))

    def search_flower(self, atr, value):
        result_flower = [flower.name for flower in self.flowers
                         if getattr(flower, atr) == value]
        return print(result_flower)


rose = Flower("rose", "red", 4, 150)
chrysant = Flower("chrysanthemum", "white", 5, 50)
bouquet = Bouquet()
bouquet.collect_flowers(rose, chrysant)
bouquet.bouquet_price()
bouquet.check_time_line()
bouquet.sort_attribute(atr="name")
bouquet.search_flower('color', 'red')
