#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self, discount=0, total=0, items=[]):
    pass
    self.discount = discount
    self._total = total
    self._items = items
  
  def getTotal(self):
    return self._total
  
  def setTotal(self, total):
    self._total = total
  
  def getItems(self):
    return self._items
  
  def setItems(self, items):
    self._items = [items]
  
  total = property(getTotal, setTotal)
  items = property(getItems, setItems)

  def add_item(self, title, price, quantity=1):
    pass
    self._total = self._total + (price * quantity)
    self.items.append(title)
  
  def apply_discount(self, discount=0.2):
    pass
    if int(self._total - (self._total * discount)) == 0:
      print("There is no discount to apply.")
    else:
      self._total = int(self._total - (self._total * discount))
      print(f"After the discount, the total comes to ${self.total}.")
