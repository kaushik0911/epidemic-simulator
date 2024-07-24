import math

class Simulation():
  def __init__(self):
    """init attributes"""
    self.day_number = 1
    self.population_size = int(input("\tEnter the population size(number of humans): "))

    root = math.sqrt(self.population_size)

    if int(root + .5)**2 != self.population_size:
      root = round(root, 0)
      self.grid_size = int(root)
      self.population_size = self.grid_size**2
      print("\tRounding population size to " + str(self.population_size) + "for visual purposes.")

    else:
      self.grid_size = int(math.sqrt(self.population_size))

    self.infection_percent = float(input("\tEnter the percentage (0-100) of the population to initially infect: "))    
    self.infection_percent /= 100

    self.infection_probability = float(input("\tEnter the probability (0-100) that a person gets infected when exposed to the disease: "))
    self.infection_duration = int(input("\tEnter the duration (in days) of the infection: "))
    self.mortality_rate = float(input("\tEnter the mortality rate (0-100) of the infection: "))
    self.sim_days = int(input("\tEnter the number of days to simulate: "))
