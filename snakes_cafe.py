print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

menu = {
  'Wings': 0,
  'Cookies':0,
  'Spring Rolls':0,
  'Salmon':0,
  'Steak':0,
  'Meat Tornado':0, 
  'A literal Garden':0,
  'Ice Cream':0,
  'Cake':0,
  'Pie':0,
  'Coffee':0,
  'Tea':0,
  'Unicorn Tears':0
}

# appetizers = ['Appetizers', '----------', 'Wings', 'Cookies', 'Spring Rolls', '']
# entrees = ['Entrees', '-----', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', '']
# desserts = ['Desserts', '--------', 'Ice Cream', 'Cake', 'Pie', '']
# drinks = ['Drinks', '------', 'Coffee', 'Tea', 'Unicorn Tears', '']

# for i in appetizers:
#     for f in entrees:
#       print(i, f)

# for i in appetizers:
#   print(appetizers)

print("\n".join(appetizers))
print("\n".join(entrees))
print("\n".join(desserts))
print("\n".join(drinks))


# for i, j in zip(appetizers, entrees):
#     print (i, j)

order = input("""***********************************
** What would you like to order? **
***********************************
>""")

print(f"Your Order: {order}")

