from models import Product, User
from datetime import datetime

class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        try:
            if self.products[product] >= amount:
                self.products[product] -= amount
                if self.products[product] == 0:
                    del self.products[product]
            else:
                raise Exception('Not Enough Products')
        except:
            raise Exception('Not Enough Products')

    def add_user(self, username):
        user = User(username)
        for users in self.users:
            if users == user:
                return None
        self.users.append(user)
        return username

    def get_total_asset(self):
        total = int()
        for name, val in self.products.items():
            total += name.price * val
        return total

    def get_total_profit(self):
        total = int()
        for user in self.users:
            total += sum([product.price for product in user.bought_products])
        return total

    def get_comments_by_user(self, user):
        msg = list()
        for products in self.products.keys():
            msg += [ com.text for com in products.comments if com.user == user]
        return msg

    def get_inflation_affected_product_names(self):
        goods = list()
        for product in self.products:
            goods += [x.name for x in self.products if x.name == product.name and x.price > product.price]
        return list(set(goods))

    def clean_old_comments(self, date):
        for product in self.products:
            product.comments = list(filter(lambda x: x.date_added > date, product.comments))

    def get_comments_by_bought_users(self, product):
        comments = list()
        for user in self.users:
            if product in user.bought_products:
                comments += [x.text for x in product.comments if x.user == user]
        return comments

# laptop = Product('laptop', 13000000, 'tech')
# macbook= Product('laptop', 25000000, 'tech')
# print(macbook)
# print(laptop)
# camera = Product('camera', 2500000, 'Pic')
# phone = Product('Phone', 7000000, 'TeCH')
# digi = Store()
# digi.add_product(laptop)
# digi.add_product(macbook)
# print(digi.get_inflation_affected_product_names())
# print(digi.products)
