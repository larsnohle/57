
width = int(input("Width? "))
length = int(input("Length? "))
area = width * length

gallons_of_paint_needed = area / 350
if area % 350 != 0:
    gallons_of_paint_needed += 1

print("You will need to purchase %d gallons of paint to cover %d square feet." % (gallons_of_paint_needed, area))
