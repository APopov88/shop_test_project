class ProductCountERROR(Exception):
    """Error raised if entered product count is not a number larger than 0"""
    def __init__(self, count, message="Count should be a number larger than 0"):
        self.count = count
        self.message = message
        super().__init__(self.message)


class PriceERROR(Exception):
    """Error raised if price entered is less than 0"""
    def __init__(self, price, message="Price should be a number not smaller than 0"):
        self.price = price
        self.message = message
        super().__init__(self.message)


merchandise = []

class Merch:
    def __init__ (self, name, count, manufacturer, price):
        self.name = name
        self.count = count
        self.manufacturer = manufacturer
        self.price = price


    def create_new_merch(name, count, manufacturer, price):
        if not count > 0:
            raise ProductCountERROR(count)

        if not price >= 0:
            raise PriceERROR(price)

        exprodindex = None
        for prod in merchandise:
            if name == prod.get("name") and manufacturer == prod.get("manufacturer"):
                exprodindex = merchandise.index(prod)

        if exprodindex:
            merchandise[exprodindex].update({
            "count": merchandise[exprodindex].get("count") + count,
            "price": price
            })
        else:
            newprod = {"name": name,
                      "count": count,
                      "manufacturer": manufacturer,
                      "price": price
                      }
            merchandise.append(newprod)

    def add_new_product():
        name = input("Enter product name")
        count = float(input("Enter product count. A number greater than 0"))
        manufacturer = input("Enter the name of the company producing the product")
        price = float(input("Enter product price, a number greater or equal to 0"))
        Merch.create_new_merch(name, count, manufacturer, price)

    def search(x):
        merchsearch = []
        for prod in merchandise:
            if x in prod.get("name") or x in prod.get("manufacturer"):
                merchsearch.append(prod)
        print(merchsearch)

    def inventory():
        inventory = []
        for prod in merchandise:
            if prod.get("count") > 0:
              inventory.append(prod)
        print(inventory)

    def supply_inventory(name, manufacturer, count):
        exprodindex = None
        for prod in merchandise:
            if name == prod.get("name") and manufacturer == prod.get("manufacturer"):
                exprodindex = merchandise.index(prod)

        if exprodindex:
            merchandise[exprodindex].update({
                "count": merchandise[exprodindex].get("count") + count,
            })
        else:
            print("Item new to shop, please use \"search\" function to find exact name of product "
                  "or initialize new inventory item with \"add_new_product()\" method")

    def price_update(name, manufacturer, price):
        exprodindex = None
        for prod in merchandise:
            if name == prod.get("name") and manufacturer == prod.get("manufacturer"):
                exprodindex = merchandise.index(prod)

        if exprodindex:
            merchandise[exprodindex].update({
                "price": price,
            })
        else:
            print("Item new to shop, please use \"search\" function to find exact name of product "
                    "or initialize new inventory item with \"add_new_product()\" method")

    def inventory_sale(name, manufacturer, count):
        exprodindex = None
        for prod in merchandise:
            if name == prod.get("name") and manufacturer == prod.get("manufacturer"):
                exprodindex = merchandise.index(prod)

        if exprodindex:
            if merchandise[exprodindex].get("count") >= count:
                merchandise[exprodindex].update({
                    "count": merchandise[exprodindex].get("count") - count,
                })
            else:
                print("Not enough items in inventory to sell, current count is: "
                      + str(merchandise[exprodindex].get("count")))
        else:
            print("Item new to shop, please use \"search\" function to find exact name")
