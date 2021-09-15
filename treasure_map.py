row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map_treasure = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
positionX = input("Where do you want to put the treasure? ")

horizontal = int(positionX[0])
vertical = int(positionX[1])

x = map_treasure[vertical - 1][horizontal - 1] = 'x'

print(f"{row1}\n{row2}\n{row3}")

