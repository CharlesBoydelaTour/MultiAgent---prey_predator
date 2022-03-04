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

}

server = ModularServer(
    WolfSheep, [canvas_element, chart_element], "Prey Predator Model", model_params
)
server.port = 8521
