print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

order_menu = {
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

appetizers = ['Appetizers', '----------', 'Wings', 'Cookies', 'Spring Rolls', '']
entrees = ['Entrees', '-----', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', '']
desserts = ['Desserts', '--------', 'Ice Cream', 'Cake', 'Pie', '']
drinks = ['Drinks', '------', 'Coffee', 'Tea', 'Unicorn Tears', '']

print("\n".join(appetizers))
print("\n".join(entrees))
print("\n".join(desserts))
print("\n".join(drinks))

print("""***********************************
** What would you like to order? **
***********************************
""")

user_selection = input('> ')

order_menu = {}

while user_selection != "quit":
    if user_selection not in order_menu:
        order_menu[user_selection] = 0
    order_menu[user_selection] +=1
    print(f" \n** {order_menu[user_selection]} order of {user_selection} have been added to your meal")
    user_selection = input('\n> ')
