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

class Cars():
    def __init__(self,registration_number,color):
        self.registration_number = registration_number
        self.color = color

class Parking():
    def __init__(self,size):
        self.size = size
        self.final_lot_size = []

    def create_parking_lot(self):
        self.final_lot_size = [None] * self.size
        return 'Created a parking lot with {} slots'.format(self.size)

    def park(self,registration_number,color):
        car_info = Cars(registration_number,color)
        car_details = '{} {}'.format(car_info.registration_number.lower() , car_info.color.lower())
        # self.car_info = '{} {}'.format(registration_number,color)
        for car_data in self.final_lot_size:
            if not car_data:
                lot_number = self.final_lot_size.index(car_data)
                self.final_lot_size[lot_number] = car_details
                return 'Allocated slot number: {}'.format(lot_number)
        return 'Sorry, parking lot is full'
    
    def leave(self,lot_number):
        if self.final_lot_size[lot_number]:
            self.final_lot_size[lot_number] = None
            return "Slot {} is free".format(lot_number)
        return "Slot {} is already free".format(lot_number)
    
    def status(self):
        pass
                

def main():
    a = Parking(5)
    b = a.create_parking_lot()
    c = a.park('mh12' , 'cars')
    d = a.park('mh122' , 'cars')
    e = a.leave(1)
    f = a.leave(4)
    print(c)
    print(d)

if __name__ == "__main__":
    main()
    