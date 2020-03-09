# Python culminating task
# Written by Hayden

def get_lot():
        lot_width  = float(input("Enter lot width(m): "))
        lot_height = float(input("Enter lot height(m): "))

        lot_area = lot_width * lot_height
        lot_frontage = lot_width
        lot_coverage = (lot_area / 836.0) * 100

        print("Lot Area:", lot_area, "m2")      
        print("Frontage: ",lot_frontage, "m" )
        print("Lot Coverage", lot_coverage, "m2")

        if(lot_area > 836.0):
                print("We have determined you: **cannot** buy this lot\n(Area too large)")
        elif(lot_frontage > 22.5):
                print("We have determined you: **cannot** buy this lot\n(Frontage too wide)")
        elif(lot_coverage > 30.0000):
                print("We have determined you: **cannot** buy this lot\n(Lot coverage over 30\%)")
        else:
                print("We have determined you: **can** buy ths lot :-)\n\n")

while(True):
        get_lot()
