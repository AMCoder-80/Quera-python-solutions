class Train:

    def __init__(self, last_visited_city, weight_capacity, is_on_trip):
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip


class Trip:

    all_cities = ('Arak', 'Ardabil', 'Urmia', 'Isfahan',
                  'Ahvaz', 'Ilam', 'Bojnord', 'Bandar Abbas',
                  'Bushehr', 'Birjand', 'Tabriz', 'Tehran',
                  'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 
                  'Sari', 'Semnan', 'Sanandaj', 'Shahr-e Kord',
                  'Shiraz', 'Qazvin', 'Qom', 'Karaj', 'Kermanshah', 
                  'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj', 'Yazd')

    def __init__(self, origin_city, destination_city, train):
        self.train = self.train_validation(train)
        self.destination_city = destination_city
        self.origin_city = self.origin_city_validation(origin_city)
        self.passengers = []
    
    def origin_city_validation(self, origin_city):
        if not origin_city in self.all_cities:
            raise Exception('This input is not a verified city!')
        elif origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")
        elif origin_city != self.train.last_visited_city:
            raise Exception('The train of the trip is not available in the origin city!')
        
        return origin_city
        
    def train_validation(self, train):
        if not isinstance(train, Train):
            raise Exception('This input is not a train!')
        elif train.is_on_trip:
            raise Exception('This train is not available!')
        
        return train

    # here implement the magic method
    
    def __call__(self):
        return self.train.weight_capacity - sum(list(map(lambda x: x.load_weight,
                                                         self.passengers)))


class Passenger:

    def __init__(self, fullname, load_weight):
        self.fullname = fullname
        self.load_weight = load_weight

    def attend_trip(self, trip):
        if self.load_weight > int(trip()):
            raise Exception('Heavy load!')
        trip.passengers.append(self)

    def cancel_trip(self, trip):
        if not self in trip.passengers:
            raise Exception('This passenger is not attended to this trip!')
        trip.passengers.remove(self)

    # here implement the magic method
    
    def __str__(self):
        return self.fullname


# raja = Train('Tehran', 250, False)

# easter = Trip('Tehran', 'Qazvin', raja)

# ali = Passenger('ali moradi', 90)
# mahsa = Passenger('mahsa saadat', 55)
# ayda = Passenger('ayda raufie', 55)

# print(easter.passengers)
# ali.attend_trip(easter)
# ayda.attend_trip(easter)
# mahsa.attend_trip(easter)
# print(easter.passengers)

