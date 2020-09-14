# Elixir of Mongoose price break down
print('Price of Mountain Silversage?')
ms = input()

print('Price of Plaguebloom?')
pb = input()

print('Price of Elixir of the Mongoose on the AH?')
potion = float(input())

final_pb = (float(pb) * 2)
final_ms = (float(ms) * 2)
final_cost = final_ms + final_pb + 0.04
roundedFinalCost = round((final_cost * 1.05), 3)
print('***Crafting cost: ' + str(roundedFinalCost))

profit = round((potion - roundedFinalCost), 3)
print('***Est. profit: ' + str(profit))

k=input("press close to exit")
