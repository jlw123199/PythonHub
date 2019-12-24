
import camelcase


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity,itemno,price))


c = camelcase.CamelCase()

txt = "a hello and world eeWIE"

print(c.hump(txt))