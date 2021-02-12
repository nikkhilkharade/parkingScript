'''
What final out put should look like
$​ create_parking_lot 6
Created a parking lot with 6 slots
$​ park KA-01-HH-1234 White Allocated slot number: 1
$​ park KA-01-HH-9999 White Allocated slot number: 2
$​ park KA-01-BB-0001 Black Allocated slot number: 3$
​ park KA-01-HH-7777 Red Allocated slot number: 4
$​ park KA-01-HH-2701 Blue Allocated slot number: 5
$​ park KA-01-HH-3141 Black Allocated slot number: 6
$​ leave 4
Slot number 4 is free
'''
class Parking():
    def __init__(self,size,slot):
        self.size = size
        self.slot = slot

    def create_parking_lot(self):
        lot_size = []
        final_lot_size = [None for x in range(self.size)]
        return 'Created a parking lot with {} slots'.format(len(self.size))
    



class Cars():
    def __init__(self,registration_number,color):
        self.registration_number = registration_number
        self.color = color
if __name__ == "__main__":
    main()
    