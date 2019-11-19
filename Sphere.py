import math

class Sphere:
    #Creating the class for the sphere
    def __init__(self , radius):
        self.radius = radius
        self.volume = (4/3) * math.pi * self.radius ** 3
        self.surfaceArea = 4 * math.pi * self.radius ** 2
    #Figuring out the radius of the sphere  
    def getRadius(self):
        return self.radius
    #Figuring out the surface area of the sphere  
    def getSurfaceArea(self):
        return self.surfaceArea
    #Figuring out the volume of the sphere    
    def getVolume(self):
        return self.volume
    #Function that creates an instance of Sphere
def main():
    radius = float(input("Enter the radius of the sphere you want to create: "))
    TheSphere = Sphere(radius)
    print("The surface area of the sphere is:" , TheSphere.getSurfaceArea())
    print("The volume of the sphere is:" , TheSphere.getVolume())
    
main()