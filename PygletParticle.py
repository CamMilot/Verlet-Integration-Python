import pyglet
import pyglet.shapes as shapes
import Particle
import numpy as np
import random
window = pyglet.window.Window()
startpos = [500,150]

radius = 15

startpoz = [startpos]
circles = []
verlets = []
shapes.Circle.opacity
length = len(startpoz)
for i in range(0,length):
    verlets.append(Particle.VerletClass(startpoz[i],radius))
    circles.append(shapes.Circle(x=startpoz[i][0], y=startpoz[i][1], radius=radius, color=(50, 225, 30)))
base = shapes.Circle(x=500,y=250,radius=225, color=(100,100,100))

      
@window.event
def on_draw():
    window.clear()
    base.draw()
    for circle in circles:
        circle.draw()
def cringe(dt):
    if len(verlets) > 100: return
    temppos = [600,250]
    temrad = 1 * random.randint(1, 20)
    startpoz.append(temppos)
    verlets.append(Particle.VerletClass(temppos,temrad))
    circles.append(shapes.Circle(x=temppos[0], y=temppos[1], radius=temrad, color=(50, 225, 30)))
def update(dt,length):
    dt = dt/2
    sub_steps = 8
    sub_dt = dt/sub_steps
    for z in range(sub_steps,0,-1):
        length = len(verlets)
        for i in range(0,length):
            verlets[i].update(sub_dt,startpoz[i])
            circles[i].x = verlets[i].position_current[0]
            circles[i].y = verlets[i].position_current[1]
        #solve collisions
        for i in range(0,length):
            object_1 = verlets[i]
            for k in range(i+1,length,1):
                object_2 = verlets[k]
                collision_axis = object_1.position_current - object_2.position_current
                distance = np.sqrt(collision_axis.dot(collision_axis))
                min_distance = object_1.radius + object_2.radius
                if (distance < min_distance):
                    n = collision_axis/distance
                    delta = min_distance - distance
                    object_1.position_current += 0.5 * delta * n
                    object_2.position_current -= 0.5 * delta * n
        
    
    
    
pyglet.clock.schedule_interval(update,.01,length)
pyglet.clock.schedule_interval(cringe,.1)
pyglet.app.run()