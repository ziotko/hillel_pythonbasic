import csv


class Product:
    def __init__(self, name, p_type, price):
        self.name = name
        self.type = p_type
        self.price = price

    def __str__(self):
        return f"{self.type.capitalize()}: {self.name}, ціна: {self.price}грн."


def combine_products(product1, product2):
    if product1.type == 'coffee' and product2.type == 'additional':
        if product2.name.lower() == 'молоко':
            latte_name = f"{product1.name} з {product2.name.lower()}"
            latte_price = product1.price + product2.price
            Product(latte_name, 'latte', latte_price)
            return latte


class Store:
    def __init__(self):
        self.products = []

    def import_products(self, filename, quantity=5):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, p_type, price = row
                product = Product(name, p_type, float(price))
                self.products.extend([product] * quantity)

    def get_products_by_type(self, p_type):
        return [product for product in self.products if product.type == p_type]

    def calculate_total_price(self):
        return sum(product.price for product in self.products)

    def sell_product(self, product):
        self.products.remove(product)


store = Store()
store.import_products('inventory .csv')

espresso = store.get_products_by_type('coffee')[0]
milk = store.get_products_by_type('additional')[0]
latte = combine_products(espresso, milk)

print(espresso)
print(milk)
print(latte)

print(f"Загальна вартість продуктів у магазині: {store.calculate_total_price()}грн.")
