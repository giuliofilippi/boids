# The screen containing th boids will be 800*800
# The code is written in python 2.7 because that is the one that
# has my version of pygame

import numpy as np
import random
import pygame
from math import atan2
from math import pi


# useful variables

# used to make animation
mp4 = False

# velocity of boids
vel = 14

# field of vision
field = 75

# Boid size
BOID_SIZE = 8


# get a random vector in dims dimensions
def get_rand_vec(dims):
    x = np.random.standard_normal(dims)
    r = np.sqrt((x*x).sum())
    return x / r

# distance between boids
def distance(bird1, bird2):
    dx = (bird1.pos-bird2.pos)[0]
    dy = (bird1.pos-bird2.pos)[1]
    return np.linalg.norm(np.array([dx,dy]))

# Get the points of triangle based on position and velocity vector
def get_triangle_points(pos,direction):

    normal = np.array([direction[1],-direction[0]])

    x1 = pos + direction * BOID_SIZE
    x2 = pos - normal * BOID_SIZE/4
    x3 = pos + normal * BOID_SIZE/4

    return [x1,x2,x3]

# Class to keep track of boid position and velocity vectors
class Boid:
    # Init function
    def __init__(self):
        x = float(random.randrange(BOID_SIZE, 800 - BOID_SIZE))
        y = float(random.randrange(BOID_SIZE, 800 - BOID_SIZE))
        self.pos = np.array([x,y])
        direction = get_rand_vec(2)
        self.velocity = vel*direction


    # Angle of given boid direction in degrees
    def angle(self):
        return atan2(self.velocity[0],self.velocity[1])*360/(2*pi)

    # Direction of boid normalised
    def direction(self):
        vec = np.array([self.velocity[0],self.velocity[1]])
        vel = np.linalg.norm(vec)
        return vec/vel

    # Points of triangle constituting a single boid
    def points(self):
        list_of_points = get_triangle_points(self.pos,self.direction())
        return list_of_points

    # neighbours of a boid
    def neighbours(self, list_of_boids):

        neighbours = []
        for brd in list_of_boids:
            if distance(self,brd)<field and brd!=self:
                neighbours.append(brd)

        return neighbours

    # update velocity based on 3 rules
    # also updates position of given boid
    def update(self, list_of_boids):

        neighbours = self.neighbours(list_of_boids)

        N = len(neighbours)

        # Rule 1 : we change a boids velocity based on neighbouring
        # boids center of mass
        if N==0:
            com = self.pos
        else:
            com = sum([x.pos for x in neighbours])/N
        move_vec1 = (com - self.pos)/75


        # Rule 2 : nearby boids repel each other
        move_vec2 = np.array([0,0])
        for bird in neighbours:
            if distance(self,bird)<15:
                move_vec2 += (self.pos - bird.pos)/4




        # Rule 3 : velocity matching. Add 1/8 of difference to nearby
        # boids velocity to each boid
        if N==0:
            vel = self.velocity
        else:
            vel = sum([x.velocity for x in neighbours])/N
        move_vec3 = (vel - self.velocity)/8


        # Changes
        self.velocity += move_vec1
        self.velocity += move_vec2
        self.velocity += move_vec3


        # Rule 5 : Stay within boundaries
        if self.pos[0] > 800 - 20:
            self.velocity[0] -= 3
        if self.pos[1] > 800 - 20:
            self.velocity[1] -= 3
        if self.pos[0] < 20:
            self.velocity[0] += 3
        if self.pos[1] < 20:
            self.velocity[1] += 3


        # Rule 4 : acceleration
        if np.linalg.norm(self.velocity) < 10:
            self.velocity = 1.1* self.velocity

        if np.linalg.norm(self.velocity) > 10:
            self.velocity = 0.9 * self.velocity

        # change position
        self.pos += self.velocity


# makes list of N random boids
def make_boids(N):
    # Function to make new random boids
    list_of_boids = []

    for i in range(N):

        boid = Boid()
        list_of_boids.append(boid)

    return list_of_boids



# make 50 boids
boid_list = make_boids(100)


def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [800, 800]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Boids")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # -------- Main Program Loop -----------
    i = 0
    while not done:
        i+=1

        if mp4 == True:
            filename = 'animation/'+'capture_'+str(i)+'.jpeg'
            pygame.image.save(screen, filename)

        # --- Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Background
        screen.fill((0,0,0))

        # --- Logic
        for boid in boid_list:

            # change boid positions and velocities based on rules
            boid.update(boid_list)

        # --- Drawing
        for boid in boid_list:
            list_of_points = boid.points()
            pygame.draw.polygon(screen, (0,206,209),list_of_points)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(20)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()













# add possibility to make videos




