from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from prey_predator.agents import Wolf, Sheep, GrassPatch
from prey_predator.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape":"circle", "Filled":"true", "Layer":1}

    if type(agent) is Sheep:
        portrayal["Color"] = "#666666"
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "white"

    elif type(agent) is Wolf:
        portrayal["Color"] = "#AA0000"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "white"

    elif type(agent) is GrassPatch:
        if agent.fully_grown:
            portrayal["Color"] = "#00AA00"
        else:
            portrayal["Color"] = "#D6F5D6"
        portrayal["Shape"] = "rect"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal


canvas_element = CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Wolves", "Color": "#AA0000"}, {"Label": "Sheep", "Color": "#666666"}]
)

model_params = {
    "grass": UserSettableParameter("checkbox", "Grass Enabled", True),
    "grass_regrowth_time": UserSettableParameter("slider", "Grass Regrowth Time", 20, 1, 100),
    "initial_sheep": UserSettableParameter("slider", "Initial Sheep Population", 50, 10, 200),
    "sheep_reproduce": UserSettableParameter("slider", "Sheep Reproduction Rate", 0.05, 0.01, 1.0,
                                             0.01),
    "initial_wolves": UserSettableParameter("slider", "Initial Wolf Population", 10, 0, 300),
    "wolf_reproduce": UserSettableParameter("slider", "Wolf Reproduction Rate", 0.02, 0.01, 1.0,
                                            0.01),
    "wolf_gain_from_food": UserSettableParameter("slider", "Wolf Gain From Food Rate", 5, 1, 50),
    "sheep_gain_from_food": UserSettableParameter("slider", "Sheep Gain From Food", 3, 1, 10),
    
    "init_energy_sheep": UserSettableParameter("slider", "Initial Energy of Sheep", 20, 1, 200),
    "init_energy_wolves": UserSettableParameter("slider", "Initial Energy of Wolf", 10, 1, 200)
    
    
}

server = ModularServer(WolfSheep, [canvas_element, chart_element], "Wolf Sheep Predation", model_params)
server.port = 8521
