import math
import random
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


#All speed units will be in meters/sec
class Car:
    def __init__(self, size = 5, speed = 20, max_speed = 30, location = 0):
        self.size = size
        self.max_speed = max_speed
        self.speed = abs(speed)
        self.location = location


    def move(self):
        self.location += self.speed
        if self.location > 1000:
            self.location = self.location % 1000
        return self.location

    def check_loc(self):
        return("I'm car {} and I'm at {}, I'm going {} m/s".format(self.car_id, self.location, self.speed))



class Road:
    def __init__(self):
        self.cars = [Car() for x in range(30)]
        self.road_map = np.array([0 for _ in range(1050)])


    def place_cars_init(self):
        placement = 0
        for car in self.cars:
            car.location = placement
            placement += 33


    def update_road_map(self):
        self.road_map = np.array([0 for _ in range(1050)])
        for car in self.cars:
            for x in range(5):
                self.road_map[car.location+x] = 1

    def change_car_speed(self):
        idx = 0
        for car in self.cars:
            space = []
            for x in self.road_map[(car.location+5):(car.location+5)+car.speed]:
                space.append(x)

            if random.random() <= .10:
                if car.speed > 0:
                    car.speed -= 2

            elif sum(space) == 0 and car.speed <= car.max_speed:
                car.speed += 2

            elif sum(space) > 0 and sum(space) <5:
                if idx == 29:
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
        return [car.speed for car in self.cars]


    def reset(self):
        self.road_map = [0 for _ in range(1050)]
        self.place_cars_init()
        self.update_road_map()



class Sim:
    def __init__(self):
        self.ticks = 0
        self.road = Road()



    def tick(self):
        road_data_sec = np.array(self.road.road_map)
        speed = self.road.check_cars()
        avg_speed = sum(speed)/len(speed)
        self.road.change_car_speed()
        self.road.drive()
        self.road.update_road_map()
        return avg_speed
        #return np.array(road_data_sec)


    def reset(self):
        return self.ticks == 0


    def run(self, num_ticks = 60):
        all_data = []
        self.road.place_cars_init()
        for tick in range(num_ticks):
            all_data.append(self.tick())
            self.ticks += 1
        #return np.array(all_data)
        return(sum(all_data)/len(all_data))
