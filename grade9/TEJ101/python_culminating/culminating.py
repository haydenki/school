
# Python culminating task
# Written by Hayden

def get_lot():
        #Get lot dismensions then calculate and print statistics
        lot_width  = float(input("Enter lot width(m): "))
        lot_height = float(input("Enter lot height(m): "))

        lot_area = lot_width * lot_height # Area
        lot_frontage = lot_width # Frontage
        lot_coverage = (978.0 / lot_area) * 100 #Percentage

        print("Lot Area:", lot_area, "m2") 
        print("Frontage: ",lot_frontage, "m" )
        print("Lot Coverage", lot_coverage, "m2")

        #Determine if lot statistics meets minimum requirements
        if(lot_area < 836.0): 
                print("We have determined you: **cannot** buy this lot\n(Area too small)")
        elif(lot_frontage < 22.5):
                print("We have determined you: **cannot** buy this lot\n(Frontage not wide enough)")
        elif(lot_coverage > 30.0000):
                print("We have determined you: **cannot** buy this lot\n(Lot coverage over 30\%)")
        else:
                print("We have determined you: **can** buy ths lot :-)")

while(True): #So I don't have to restart the program every time I want to test different inputs
    get_lot()


