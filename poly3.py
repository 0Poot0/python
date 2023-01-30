class vehical:
    def seatingcapacity(self):
        print("The seating capacity is 4.")
class bus(vehical):
    def seatingcapacity(self):
        print("The seating capacity is 50.")

class car1(vehical):
    pass
class car2(vehical):
    pass

objvehical=vehical()
objcar1=car1()
objcar2=car2()
objbus=bus()

objbus.seatingcapacity()
objcar1.seatingcapacity()
objcar2.seatingcapacity()

