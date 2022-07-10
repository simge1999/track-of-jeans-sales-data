stock = 1000
jeans_sold=400
target = 600
target_hit = target - jeans_sold
print("you have to sell --- to reach your target:")
print(target_hit)
current_stock = stock - jeans_sold
print("jeans in stock:")
print(current_stock)
available = True 
if available:
  print("in stock")
  if not available:
    print("out of stock")