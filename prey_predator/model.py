"""
Prey-Predator Model
================================

Replication of the model found in NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Sheep Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
"""

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from prey_predator.agents import Sheep, Wolf, GrassPatch
from prey_predator.schedule import RandomActivationByBreed
import random

class WolfSheep(Model):
    """
    Wolf-Sheep Predation Model
    """

    height = 20
    width = 20

    initial_sheep = 100
    initial_wolves = 50

    sheep_reproduce = 0.04
    wolf_reproduce = 0.05

    wolf_gain_from_food = 20

    grass = False
    grass_regrowth_time = 30
    sheep_gain_from_food = 4

    description = (
        "A model for simulating wolf and sheep (predator-prey) ecosystem modelling."
    )

    def __init__(
        self,
        height=20,
        width=20,
        initial_sheep=100,
        initial_wolves=50,
        sheep_reproduce=0.04,
        wolf_reproduce=0.05,
        wolf_gain_from_food=20,
        grass=False,
        grass_regrowth_time=30,
        sheep_gain_from_food=4,
    ):
        """
        Create a new Wolf-Sheep model with the given parameters.

        Args:
            initial_sheep: Number of sheep to start with
            initial_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: Probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
            grass: Whether to have the sheep eat grass for energy
            grass_regrowth_time: How long it takes for a grass patch to regrow
                                 once it is eaten
            sheep_gain_from_food: Energy sheep gain from grass, if enabled.
        """
        super().__init__()
        # Set parameters
        self.height = height
        self.width = width
        self.initial_sheep = initial_sheep
        self.initial_wolves = initial_wolves
        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.sheep_gain_from_food = sheep_gain_from_food

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.datacollector = DataCollector(
            {
                "Wolves": lambda m: m.schedule.get_breed_count(Wolf),
                "Sheep": lambda m: m.schedule.get_breed_count(Sheep),
            }
        )

        # Create sheep:
        # ... to be completed
        init_energy_sheep = 40
        for i_s in range(self.initial_sheep):
            init_x, init_y = random.randrange(self.width), random.randrange(self.height)
            s = Sheep(i_s, (init_x, init_y), self,moore=True, energy=init_energy_sheep)
            self.grid.place_agent(s, (init_x, init_y))
            self.schedule.add(s)
        # Create wolves
        # ... to be completed
        init_energy_wolves = 10
        for i_w in range(self.initial_wolves):
            init_x, init_y = random.randrange(self.width), random.randrange(self.height)
            w = Wolf(self.initial_sheep+i_w, (init_x, init_y), self,moore=True ,energy=init_energy_wolves)
            self.grid.place_agent(w, (init_x, init_y))
            self.schedule.add(w)

        # Create grass patches
        # ... to be completed
        i_g = 0
        for x in range(self.width):
            for y in range(self.height):
                g = GrassPatch(self.initial_sheep+self.initial_wolves+i_g, (x,y), self, self.grass, self.grass_regrowth_time)
                i_g += 1
                self.grid.place_agent(g, (x, y))
                self.schedule.add(g)
    
        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()

        # Collect data
        self.datacollector.collect(self)

        # ... to be completed
        # reproduction

    def run_model(self, step_count=200):

        # ... to be completed
        for _ in range(step_count):
            self.step()

