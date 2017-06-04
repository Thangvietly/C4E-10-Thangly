import pygame
class Point():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def distant(self, other_point):
        dx = (self.x - other_point.x)
        dy = (self.y - other_point.y)
        distant = (dx**2 + dy**2)**(1/2)
        return distant

    def halfway(self, other_point):
        self.half_x = (self.x + other_point.x)/2
        self.half_y = (self.y + other_point.y)/2
        print("Halfway point: ({0}, {1})".format(self.half_x, self.half_y))
        return self.half_x, self.half_y

    def reflect_x(self):
        self.reflect_x = self.x
        self.reflect_y = -(self.y)
        print("Reflect Ox: ({0},{1})".format(self.reflect_x, self.reflect_y))

    def reflect_y(self):
        self.reflect_x = -(self.x)
        self.reflect_y = self.y
        print("Reflect Oy: ({0},{1})".format(self.reflect_x,self.reflect_y))

    def reflect_origin(self):
        self.reflect_x = -(self.x)
        self.reflect_y = -(self.y)
        print("Reflect O: ({0},{1})".format(self.reflect_x, self.reflect_y))
class Rectangle:
    def __init__(self,point_a, point_b, point_d):
        self.width = point_a.distant(point_b)
        self.height = point_a.distant(point_d)
        print("Width = {0} \nHeight = {1}".format(self.width, self.height))
    def area(self):
        self.area = self.width*self.height
        print("Area: ",self.area)
    def perimeter(self):
        self.perimeter = (self.width + self.height)*2
        print("Perimeter: ", self.perimeter)
    def flip(self):
        (self.width, self.height) = (self.height, self.width)
        print("After Flip: width = {0}, height = {1}".format(self.width, self.height))

print("Cau1: ")
point = Point(2,1)
other_point = Point(10,9)
Point.distant(point,other_point)
print("Distant: ",Point.distant(point, other_point))
Point.halfway(point,other_point)
Point.reflect_x(point)
Point.reflect_y(point)
Point.reflect_origin(point)

print("Cau2: ")
point_a = Point(2,1)
point_b = Point(10,9)
point_d = Point(-5,-2)
print("Point_a: ({0},{1}) ; Point_b:({2},{3}) ; Point_d: ({4},{5}) ".format
      (point_a.x,point_a.y,point_b.x,point_b.y,point_d.x,point_d.y))

HCN = Rectangle(point_a,point_b,point_d)
HCN.area()
HCN.perimeter()
HCN.flip()