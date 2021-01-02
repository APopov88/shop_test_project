merchandise = {}


class Merch:
  def __init__ (self, name, count):
    self.name = name
    self.count = count
    if name in merchandise.keys():
      merchandise.update({name: merchandise.get(name)+count})
    else:
      merchandise.update({name:count})

  def search(x):
    merchsearch = {}
    for key in merchandise.keys():
      if x in key:
        merchsearch.update({key: merchandise.get(key)})
    print(merchsearch)

  def inventory():
    inventory = {}
    for (key, value) in merchandise.items():
      if value > 0:
        inventory.update({key: value})
    print(inventory)

  def add_inventory(name, count):
    if name in merchandise.keys():
      merchandise.update({name: merchandise.get(name) + count})
    else:
      print("Item new to shop, please initialize new inventory item")

  def sale(name, count):
      if name in merchandise.keys():
        merchandise.update({name: merchandise.get(name) - count})
      else:
        print("Item not in inventory, impossible to sell")


cucumber = Merch("Cucumber", 50)

tomatoe = Merch("Tomatoe", 55)

cucumber = Merch("Cucumber", 20)

Onion = Merch("Onion",10)

Merch.add_inventory("Tomatoe", 15)

Merch.sale("Tomatoe", 2)

Merch.inventory()



