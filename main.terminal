import random

class Simulation():
  def __init__(self):
    """init attributes"""
    self.day_number = 1

    print("To simulate an epidemic outbreak, we must know the population size.")
    self.population_size = int(input("\tEnter the population size: "))

    print("\nWe must first start by infecting a portion of the population.")
    self.infection_percent = float(input("\tEnter the percentage (0-100) of the population to initially infect: "))

    self.infection_percent /= 100

    print("\nWe must know the risk a person has to contract the disease when exposed.")

    self.infection_probability = float(input("\tEnter the probability (0-100) that a person gets infected when exposed to the disease: "))

    print("\nWe must know how long the infection will last when exposed.")
    self.infection_duration = int(input("\tEnter the duration (in days) of the infection: "))

    print("\nWe must know the mortality rate of those infected.")
    self.mortality_rate = float(input("\tEnter the mortality rate (0-100) of the infection: "))

    print("\nWe must know how long to run the simulation.")
    self.sim_days = int(input("\tEnter the number of days to simulate: "))

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

class Population():
  def __init__(self, simulation):
    """init attributes"""
    self.population = []

    for i in range(simulation.population_size):
      person = Person()
      self.population.append(person)

  def initial_infection(self, simulation):
    infected_count = int(round(simulation.infection_percent*simulation.population_size, 0))

    for i in range(infected_count):
      self.population[i].is_infected = True
      self.population[i].days_infected = 1

    random.shuffle(self.population)

  def spread_infection(self, simulation):
    for i in range(len(self.population)):
      if self.population[i].is_dead == False:
        if i == 0:
          if self.population[i+1].is_infected:
            self.population[i].infect(simulation)
        elif i < len(self.population)-1:
          if self.population[i-1].is_infected or self.population[i+1].is_infected:
            self.population[i].infect(simulation)
        elif i == len(self.population)-1:
          if self.population[i-1].is_infected:
            self.population[i].infect(simulation)

  def update(self, simulation):
    simulation.day_number += 1
    for person in self.population:
      person.update(simulation)

  def display_statistics(self, simulation):
    total_infected_count = 0
    total_death_count = 0

    for person in self.population:
      if person.is_infected:
        total_infected_count += 1
        if person.is_dead:
          total_death_count += 1

    infected_percent = round(100*(total_infected_count / simulation.population_size), 4)
    death_percent    = round(100*(total_death_count / simulation.population_size), 4)

    print("\n-----Day # " + str(simulation.day_number) + "-----")
    print("Percentage of Population Infected: " + str(infected_percent) + "%")
    print("Percentage of Population Dead: " + str(death_percent) + "%")
    print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation.population_size))
    print("Total Deaths: " + str(total_death_count) + " / " + str(simulation.population_size))

  def graphics(self):
    status = []
    for person in self.population:
      if person.is_dead:
        char = 'X'
      else:
        if person.is_infected:
          char = 'I'
        else:
          char = 'O'

      status.append(char)

    for letter in status:
      print(letter, end='-')

sim = Simulation()
pop = Population(sim)

pop.initial_infection(sim)
pop.display_statistics(sim)
pop.graphics()
input("\nPress enter to begin the simulation")

for i in range(1, sim.sim_days):
  pop.spread_infection(sim)
  pop.update(sim)
  pop.display_statistics(sim)
  pop.graphics()

  if i != sim.sim_days - 1:
    input("\nPress enter to advance to the next day.")