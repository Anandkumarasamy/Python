
items_cost = [1000, 2000, 3000, 3000,2000,10000,7000,1000,5000,6000,900,8000]

items_cost_with_gst=map(lambda X: X+50,items_cost)

print('Iteam cost are:',items_cost)

print('iteam cost with gst:',list(items_cost_with_gst))