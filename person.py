import random

class Person():
  def __init__(self):
    """init attributes"""
    self.is_infected = False
    self.is_dead = False
    self.days_infected = 0

  def infect(self, simulation):
    #chance of infect
    if random.randint(0, 100) < simulation.infection_probability:
      self.is_infected = True

  def heal(self):
    self.is_infected = False
    self.days_infected = 0

  def die(self):
    self.is_dead = True

  def update(self, simulation):
    if not self.is_dead:
      if self.is_infected:
        self.days_infected += 1
  
        if random.randint(0, 100) < simulation.mortality_rate:
          self.die()
        elif self.days_infected == simulation.infection_duration:
          self.heal()