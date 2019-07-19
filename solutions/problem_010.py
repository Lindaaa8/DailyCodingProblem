

print("Hello")

def calculate_price(supplier,base_price,day):
  price = base_price
  if supplier == 'A' and day == 1:
    price = 1.5 * base_price
  elif supplier == 'C' and day >= 7:
    price = 0.9 * base_price
  elif supplier == 'D' and day < 7:
    price = 1.1 * base_price
  price = float("{0:.2f}".format(price))
  return price



def get_price(suppliers):
  prices = []
  n = len(suppliers)
  if n == 0:
    return None
  for i in range(n):
    supplier = suppliers[i][0]
    base_price = suppliers[i][1]
    day = suppliers[i][2]
    if supplier == 'B' and day >= 3 or supplier !='B':
      price = calculate_price(supplier,base_price,day)
      prices.append(price)
  if len(prices) == 0:
    return None
  prices.sort()
  return prices


def find_hotels(n,suppliers, m, users):
  results = []
  for i in range(m):
    available_suppliers = []
    for j in range(n):
      supplier = suppliers[j]
      user = users[i]
      supplier_city = supplier[0]
      user_city = user[0]
      if supplier_city == user_city:
        available_suppliers.append([supplier[1],supplier[2],user[1]])
    prices_i = get_price(available_suppliers)
    results.append(prices_i)
  return results


find_hotels(7,
[["Toronto","A",100.00],
["North York","B",250],
["Waterloo","C",19.99],
["Toronto","D",100.00],
["Kitchener","F",25],
["Kitchener","F",24],
["Kitchener","F",25]],
4,
[["Toronto",1],
["North York",2],
["Waterloo",8],
["Kitchener",10]])