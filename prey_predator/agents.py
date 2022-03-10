from re import A
from mesa import Agent
from torch import isin
from prey_predator.random_walk import RandomWalker
import random
class Sheep(RandomWalker):
    """
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        self.pos = pos
        
    def eat_grass(self):
        #function that return what is in cell pos
        agents = self.model.grid.get_cell_list_contents(self.pos)
        for agent in agents:
            if isinstance(agent, GrassPatch):
                grass_patch = agent
        if grass_patch.fully_grown:
            self.energy += self.model.sheep_gain_from_food
            grass_patch.fully_grown = False 
            grass_patch.countdown = 30
            
    def step(self):
        """
        A model step. Move, then eat grass and reproduce.
        """
        self.random_move()
        # ... to be completed
        self.energy -=1 
        self.eat_grass()
        if self.energy <= 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
        
        prob_reproduce = random.random()    
        if prob_reproduce >= 1-self.model.sheep_reproduce:
            lamb = Sheep(self.model.idx, self.pos, self.model, self.moore, self.energy/2)
            self.model.idx += 1
            self.model.grid.place_agent(lamb, lamb.pos)
            self.model.schedule.add(lamb)
            self.energy = self.energy/2
        


class Wolf(RandomWalker):
    """
    A wolf that walks around, reproduces (asexually) and eats sheep.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        self.pos = pos
        
    def eat_sheep(self):
        #function that return what is in cell pos
        agents = self.model.grid.get_cell_list_contents(self.pos)
        for agent in agents:
            if isinstance(agent, Sheep):
                self.energy += self.model.wolf_gain_from_food
                self.model.grid._remove_agent(self.pos, agent)
                self.model.schedule.remove(agent) #il va tous les manger

    def step(self):
        self.random_move()
        # ... to be completed
        self.energy -=1 
        self.eat_sheep()
        if self.energy <= 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
        
        prob_reproduce = random.random()    
        if prob_reproduce >= 1-self.model.wolf_reproduce:
            wolf = Wolf(self.model.idx, self.pos, self.model, self.moore, self.energy/2)
            self.model.idx += 1
            self.model.grid.place_agent(wolf, wolf.pos)
            self.model.schedule.add(wolf)
            self.energy = self.energy/2
        

class GrassPatch(Agent):
    """
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    """

    def __init__(self, unique_id, pos, model, fully_grown, countdown):
        """
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        """
        super().__init__(unique_id, model)
        # ... to be completed
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.pos = pos
    def step(self):
        # ... to be completed
        self.countdown -= 1
        if self.countdown == 0:
            self.fully_grown = True