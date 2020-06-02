import tkinter
from simulation import Simulation
from population import Population

def graphics(simulation, population, canvas):
  square_dimension = 600//simulation.grid_size

  for i in range(simulation.grid_size):
    y = i*square_dimension
    for j in range(simulation.grid_size):
      x = j*square_dimension

      if population.population[i][j].is_dead:
        canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='red')
      else:
        if population.population[i][j].is_infected:
          canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='yellow')
        else:
          canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='green')

sim = Simulation()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

pop = Population(sim)
pop.initial_infection(sim)
pop.display_statistics(sim)
input("Press Enter to begin simulation.")
for i in range(1, sim.sim_days):
  pop.spread_infection(sim)
  pop.update(sim)
  pop.display_statistics(sim)
  graphics(sim, pop, sim_canvas)

  sim_window.update()

  if i != sim.sim_days-1:
    sim_canvas.delete('all')
