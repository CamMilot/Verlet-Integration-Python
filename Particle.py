import numpy as np

class VerletClass:
    def __init__(self,startpos,radius) -> None:
        self.position_current = np.array(startpos)
        self.position_old = np.array(startpos)
        self.acceleration = np.array([0,-5000])
        self.gravity = np.array([0,-5000])
        self.radius = radius
        
    def updatePosition(self,dt):
        velocity = self.position_current - self.position_old
        # Save current position
        self.position_old = self.position_current
        # Perform Verlet Integration
        self.position_current = self.position_current + velocity + self.acceleration * dt * dt
        # Reset acceleration
        self.acceleration = np.array([0,0])
    def update(self,dt,pos):
        self.applyGravity()
        self.applyConstraint(pos)
        self.updatePosition(dt)
        
    def accelerate(self,acc):
        self.acceleration = self.acceleration + acc
        
    def applyGravity(self):
        self.accelerate(self.gravity)
        
    def applyConstraint(self,pos):
        position = np.array([500,250])
        radius = 225
        to_obj = self.position_current - position
        distance = np.sqrt(to_obj.dot(to_obj))
        if (distance > (radius - self.radius)):
            n = to_obj / distance
            #print(n * (distance - 50))
            self.position_current = position + n * (radius - self.radius)
    
        
        