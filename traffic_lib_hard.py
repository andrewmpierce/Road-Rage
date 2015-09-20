import math
import random
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


#All speed units will be in meters/sec
class Car:
    def __init__(self, size = 5, speed = 5, max_speed = 15, location = 0, accel = 2, init_slow = .10, slow_down = .10):
        self.size = size
        self.max_speed = max_speed
        self.speed = abs(speed)
        self.location = location
        self.accel = accel
        self.slow_down = slow_down
        self.init_slow = init_slow
        self.distance = self.speed


    def move(self):
        self.location += self.speed
        if self.location > 7000:
            self.location = self.location % 7000
        return self.location


    def rough_road(self):
        if self.location >= 1000 and self.location < 1030:
            self.slow_down = self.slow_down * 1.4

        elif self.location >= 2000 and self.location < 2500:
            self.slow_down == self.init_slow

        elif self.location >= 3000 and self.location < 3030:
            self.slow_down = self.slow_down * 2

        elif self.location > 4000 and self.location < 4500:
            self.slow_down == self.init_slow

        elif self.location >= 5000 and self.location < 5030:
            self.slow_down = self.slow_down * 1.2

        elif self.location > 6000 and self. location < 6500:
            self.slow_down == self.init_slow
        return self.slow_down


    def check_loc(self):
        return("I'm at {}, I'm going {} m/s, my slow down is {} ".format(self.location, self.speed, self.slow_down))


class Aggressive(Car):
    def __init__(self, size = 5, speed = 5, max_speed = 15, location = 0, accel = 5, init_slow = .05, slow_down = .05):
        super().__init__(size, speed, max_speed, location, accel, init_slow, slow_down)
        self.size = size
        self.max_speed = max_speed
        self.speed = abs(speed)
        self.location = location
        self.accel = accel
        self.slow_down = slow_down
        self.init_slow = init_slow
        self.distance = self.speed


class Commercial(Car):
    def __init__(self, size = 25, speed = 5, max_speed = 15, location = 0, accel = 1.5, init_slow = .10, slow_down = .10):
        super().__init__(size, speed, max_speed, location, accel, init_slow, slow_down)
        self.size = size
        self.max_speed = max_speed
        self.speed = abs(speed)
        self.location = location
        self.accel = accel
        self.slow_down = slow_down
        self.init_slow = init_slow
        self.distance = (self.speed * 2)



class Road:
    def __init__(self):
        self.cars = self.make_cars()
        self.road_map = np.array([0 for _ in range(7050)])


    def make_cars(self):
        cars = []
        for x in range(150):
            random_pick = random.random()
            if random_pick <= .10:
                cars.append(Aggressive(Car))
            elif random_pick > .10 and random_pick <= .25:
                cars.append(Commercial(Car))
            else:
                cars.append(Car())
        return cars

    def place_cars_init(self):
        placement = 0
        for car in self.cars:
            car.location = placement
            placement += 45


    def update_road_map(self):
        self.road_map = np.array([0 for _ in range(7050)])
        for car in self.cars:
            if car.size == 5:
                for x in range(5):
                    self.road_map[car.location+x] = 1
            else:
                for x in range(25):
                    self.road_map[car.location+x] = 1


    def change_car_speed(self):
        idx = 0
        for car in self.cars:
            space = []
            if car.size == 5:
                for x in self.road_map[(car.location+5): (car.location+5) + car.distance]:
                    space.append(x)
            else:
                for x in self.road_map[(car.location+25): (car.location+25) + car.distance]:
                    space.append(x)

            if random.random() <= car.rough_road():
                if car.speed > 2:
                    car.speed -= 2

            elif sum(space) == 0 and car.speed >= car.max_speed:
                car.speed == car.max_speed

            elif sum(space) == 0 and car.speed <= car.max_speed:
                car.speed += car.accel

            elif sum(space) > 0 and sum(space) < 5:
                if idx == 149:
                    car.speed = self.cars[0].speed
                else:
                    car.speed = self.cars[idx+1].speed

            elif sum(space) > 5:
                if car.speed > 0:
                    car.speed = 0
            idx+=1


    def drive(self):
        return [car.move() for car in self.cars]


    def check_cars(self):
        return [car.check_loc() for car in self.cars]

    def speed_cars(self):
        return [car.speed for car in self.cars]




class Sim:
    def __init__(self):
        self.ticks = 0
        self.road = Road()


    def tick(self):
        road_data_sec = np.array(self.road.road_map)
        speed = self.road.speed_cars()
        avg_speed = sum(speed)/len(speed)
        self.road.change_car_speed()
        self.road.drive()
        self.road.update_road_map()
        return(avg_speed, road_data_sec)


    def run(self, num_ticks = 60):
        all_data = []
        avg_speed_data = []
        self.road.place_cars_init()
        for tick in range(num_ticks):
            all_data.append(self.tick()[1])
            avg_speed_data.append(self.tick()[0])
            self.ticks += 1
        avg_speed_data = sum(avg_speed_data)/len(avg_speed_data)
        return(np.array(all_data), avg_speed_data)
