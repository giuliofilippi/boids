# boids
Boids is a term invented by Craig Reynolds in 1986 ([Wikipedia](https://en.wikipedia.org/wiki/Boids)). It describes computer generated objects following simple 
rules that ultimately show group behaviour. This example is of interest because it shows how objects following
very simple rules can act as a group, this phenomenon is called emergence.

The three main rules these boids follow :

* **separation** : steer to avoid crowding local flockmates
* **alignment** : steer towards the average heading of local flockmates
* **cohesion** : steer to move towards the average position (center of mass) of local flockmates

Programming these Boids is a simple and popular exercise. Here I show my own implementation in python and pygame along with 
some videos of these boid's behaviour.
