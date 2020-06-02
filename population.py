import random
from person import Person

class Population():

  def __init__(self, simulation):
    """init attributes"""
    self.population = []
    
    for i in range(simulation.grid_size):
      row = []
      for j in range(simulation.grid_size):
        person = Person()
        row.append(person)
      self.population.append(row)


  def initial_infection(self, simulation):
    infected_count = int(round(simulation.infection_percent*simulation.population_size, 0))
    infections = 0

    while infections < infected_count:
      x = random.randint(0, simulation.grid_size - 1)
      y = random.randint(0, simulation.grid_size - 1)

      if not self.population[x][y].is_infected:
        self.population[x][y].is_infected = True
        self.population[x][y].days_infected = 1
        infections += 1

  def spread_infection(self, simulation):

    for i in range(simulation.grid_size):
      for j in range(simulation.grid_size):
        if self.population[i][j].is_dead == False:
          if i == 0:
            if j == 0:
              if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                self.population[i][j].infect(simulation)
            elif j == simulation.grid_size-1:
              if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                self.population[i][j].infect(simulation)
            else:
              if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                self.population[i][j].infect(simulation)
          elif i == simulation.grid_size-1:
            if j == 0:
              if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)
            elif j == simulation.grid_size-1:
              if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)
            else:
              if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)
          else:
            if j == 0:
              if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)
            elif j == simulation.grid_size-1:
              if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)
            else:
              if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                self.population[i][j].infect(simulation)


  def update(self, simulation):
    simulation.day_number += 1
    for row in self.population:
      for person in row:
        person.update(simulation)

  def display_statistics(self, simulation):
    total_infected_count = 0
    total_death_count = 0

    for row in self.population:
      for person in row:
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

