import pygame
import froggerlib
import random


class Frogger:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
 
        lane_size = (self.mHeight/11)
 
        x = self.mWidth*0.46
        y = 10.1*lane_size
        speed = self.mWidth / (3*30.0)
        self.frog = (froggerlib.Frog(x, y, 0.8 * lane_size, 0.8 * lane_size,
                                     x, y, speed, lane_size, lane_size), (255, 255, 255))

        self.stages = []
        
        color = (201, 44, 44)
        y = 10*lane_size
        stage = (froggerlib.Stage(0, y, self.mWidth, lane_size), color)
        self.stages.append(stage)

        y = 5 * lane_size
        stage = stage = (froggerlib.Stage(0, y, self.mWidth, lane_size), color)
        self.stages.append(stage)
 
        self.waters = []
        self.turtles = []
        self.logs = []
        self.roads = []
        self.cars = []
        self.grasses = []
        self.homes = []

        x = self.mWidth / 7
        color = (50, 100, 200)
        y = 0
        h = lane_size
        w = self.mWidth / 7
        for i in range(3):
            home = (froggerlib.Home(x, y, w, h), color)
            self.homes.append(home)
            x += (w * 2)

        x = 0
        color = (37, 173, 19)
        for i in range(4):
            grass = (froggerlib.Grass(x, y, w, h) , color)
            self.grasses.append(grass)
            x += (w * 2)


        lane1 = { 'number': 1,
                 'n_objs': 4,
                 'obj_width': 0.05*self.mWidth,
                 'obj_speed': self.mWidth / (5.5*30.0),
                 'obj_type': 'turtle',
                 'obj_direction': 'right',
                 'obj_color': (91, 201, 44),
                 'lane_type': 'water'}

        lane2 = { 'number': 2,
                 'n_objs': 2,
                 'obj_width': 0.20*self.mWidth,
                 'obj_speed': self.mWidth / (5.5*30.0),
                 'obj_type': 'log',
                 'obj_direction': 'left',
                 'obj_color': (139,69,19),
                 'lane_type': 'water'}

        lane3 = { 'number': 3,
                 'n_objs': 5,
                 'obj_width': 0.05*self.mWidth,
                 'obj_speed': self.mWidth / (5.5*30.0),
                 'obj_type': 'turtle',
                 'obj_direction': 'right',
                 'obj_color': (91, 201, 44),
                 'lane_type': 'water'}

        lane4 = { 'number': 4,
                 'n_objs': 2,
                 'obj_width': 0.20*self.mWidth,
                 'obj_speed': self.mWidth / (5.5*30.0),
                 'obj_type': 'log',
                 'obj_direction': 'left',
                 'obj_color': (139,69,19),
                 'lane_type': 'water'}

        lane6 = { 'number': 6,
                 'lane_color': (100, 100, 100),
                 'n_objs': 2,
                 'obj_width': 0.20*self.mWidth,
                 'obj_speed': self.mWidth / (5.5*30.0),
                 'obj_color': (200,200,200),
                 'obj_type': 'truck',
                 'obj_direction': 'right',
                 'lane_type': 'road'
        }
        lane7 = { 'number': 7,
                 'lane_color': (60, 60, 60),
                 'n_objs': 1,
                 'obj_width': 0.10*self.mWidth,
                 'obj_speed': self.mWidth / (2.0*30.0),
                 'obj_color': (200,0,0),
                 'obj_type': 'RaceCar',
                 'obj_direction': 'left',
                 'lane_type': 'road'
        }
        lane8 = { 'number': 8,
                 'lane_color': (100, 100, 100),
                 'n_objs': 4,
                 'obj_width': 0.10*self.mWidth,
                 'obj_speed': self.mWidth / (6.0*30.0),
                 'obj_color': (200,200,70),
                 'obj_type': 'dozer',
                 'obj_direction': 'right',
                 'lane_type': 'road'
        }
        lane9 = { 'number': 9,
                 'lane_color': (60, 60, 60),
                 'n_objs': 3,
                 'obj_width': 0.08*self.mWidth,
                 'obj_speed': self.mWidth / (3*30.0),
                 'obj_color': (0,120,80),
                 'obj_type': 'car',
                 'obj_direction': 'left',
                 'lane_type': 'road'
        }

        color = (50, 100, 200)
        for lane in [lane1, lane2, lane3, lane4, lane6, lane7, lane8, lane9]:
            y = lane['number']*lane_size
            if lane['lane_type'] == 'road':
                road = (froggerlib.Road(0, y, self.mWidth, lane_size), lane['lane_color'])
                self.roads.append(road)
            else:
                water = (froggerlib.Water(0, y, self.mWidth, lane_size), color)
            self.waters.append(water)

            x = random.randrange(0, self.mWidth)
            for i in range(lane['n_objs']):
                x += self.mWidth/lane['n_objs']
                if x >= self.mWidth:
                    x -= self.mWidth
                w = lane['obj_width']
                y = (lane['number']+0.1)*lane_size
                speed = lane['obj_speed']
                if lane['obj_direction'] == 'right':
                    desired_x = self.mWidth
                else:
                    desired_x = -w
                obj_type = lane['obj_type']
                if obj_type == 'RaceCar':
                    speed1 = 0.5*speed
                    speed2 = 2.0*speed
                    car =  (froggerlib.RaceCar(x, y, w, 0.8*lane_size, desired_x, y, speed1, speed2), lane['obj_color'])
                    self.cars.append(car)
                elif obj_type == 'truck':
                    car =  (froggerlib.Truck(x, y, w, 0.8*lane_size, desired_x, y, speed), lane['obj_color'])
                    self.cars.append(car)
                elif obj_type == 'car':
                    car =  (froggerlib.Car(x, y, w, 0.8*lane_size, desired_x, y, speed), lane['obj_color'])
                    self.cars.append(car)
                elif obj_type == 'dozer':
                    car =  (froggerlib.Dozer(x, y, w, 0.8*lane_size, desired_x, y, speed), lane['obj_color'])
                    self.cars.append(car)
                elif obj_type == 'turtle':
                    obj = (froggerlib.Turtle(x, y, w, 0.8*lane_size, desired_x, y, speed), lane['obj_color'])
                    self.turtles.append(obj)
                elif obj_type == 'log':
                    obj = (froggerlib.Log(x, y, w, 0.8*lane_size, desired_x, y, speed), lane['obj_color'])
                    self.logs.append(obj)
        self.mGameOver = False
        return
 
    def evolve(self, keys, dt):
        if self.mGameOver:
            return
         
        if pygame.K_UP in keys:
            self.frog[0].up()
        if pygame.K_DOWN in keys:
            self.frog[0].down()
        if pygame.K_LEFT in keys:
            self.frog[0].left()
        if pygame.K_RIGHT in keys:
            self.frog[0].right()
        self.frog[0].move()
 
 
        for car in self.cars:
            car[0].move()
            if car[0].atDesiredLocation():
                if car[0].getDesiredX() < 0:
                    car[0].setX(self.mWidth+1)
                else:
                    car[0].setX(-car[0].getWidth())
            if car[0].hits(self.frog[0]):
                self.mGameOver = True

        if self.frog[0].outOfBounds(self.mWidth, self.mHeight):
            self.mGameOver = True

        for obj in self.turtles:
            obj[0].move()
            if obj[0].atDesiredLocation():
                if obj[0].getDesiredX() < 0:
                    obj[0].setX(self.mWidth + 1)
                else:
                    obj[0].setX(-obj[0].getWidth())
            obj[0].supports(self.frog[0])

        for obj in self.logs:
            obj[0].move()
            if obj[0].atDesiredLocation():
                if obj[0].getDesiredX() < 0:
                    obj[0].setX(self.mWidth + 1)
                else:
                    obj[0].setX(-obj[0].getWidth())
            obj[0].supports(self.frog[0])

        for water in self.waters:
            if water[0].hits(self.frog[0]):
                self.mGameOver = True

        if self.frog[0].outOfBounds(self.mWidth, self.mHeight):
            self.mGameOver = True

        for home in self.homes:
            if home[0].containsLocatable(self.frog[0]):
                self.mGameOver = True

        for grass in self.grasses:
            if grass[0].overlapWithLocatable(self.frog[0]):
                self.mGameOver = True

        return
        
    def draw_object(self, surface, data):
        obj, color = data
        x = obj.getX()
        y = obj.getY()
        w = obj.getWidth()
        h = obj.getHeight()
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(surface, color, rect, 0)
        return

    def draw( self, surface ):
        for stage in self.stages:
            self.draw_object(surface, stage)
        for road in self.roads:
            self.draw_object(surface, road)
        for water in self.waters:
            self.draw_object(surface, water)
        for home in self.homes:
            self.draw_object(surface, home)
        for grass in self.grasses:
            self.draw_object(surface, grass)
        for car in self.cars:
            self.draw_object(surface, car)
        for turtle in self.turtles:
            self.draw_object(surface, turtle)
        for log in self.logs:
            self.draw_object(surface, log)
        self.draw_object(surface, self.frog)
        
        return
 