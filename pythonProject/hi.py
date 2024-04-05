
Item_name = input("what is your item name")

price = input("what is your price")

size_of_item= len(Item_name) + len(price)
print(size_of_item)
tog = '.' * (25 - size_of_item)

print(Item_name, tog, price)