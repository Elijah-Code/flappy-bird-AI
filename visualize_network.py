import pygame
from neat import Pool
import random
import matplotlib.pyplot as plt 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150,150,150)
GREEN = (0,255,0)



class Neuron:
    def __init__(self, pos, radius=5, color=WHITE):
        self.radius = radius
        self.pos = pos
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


class Connection:
    def __init__(self, start_pos, end_pos, width=3, color=GRAY):
        self.color = color
        self.width = width
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)


class Visualizer:
    def __init__(self, pool, size, scale=2, space=5):
        self.size = size
        self.space = space
        self.scale = scale
        self.population = pool.population
        self.surface = pygame.surface.Surface(self.size)

    @property
    def network(self):
        return self.population[-1].network

    def visualize(self):
        neurons = {}

        for x, layer in enumerate(self.network.layers):
            for y, neuron in enumerate(layer):

                if neuron.enabled and neuron.type == "output":                    
                    color = (255,0,0)
                elif neuron.enabled and neuron.type != "output":
                    color = (255,255,255)

                pos = [self.space + x*self.scale, self.space + y*self.scale]
                neuron_repr = Neuron(pos, radius=5, color=color)
                neurons[neuron.id] = neuron_repr
                neuron_repr.draw(self.surface)

        for conn in self.network.conns:
            start_neuron = neurons[conn.in_neuron.id]
            out_neuron = neurons[conn.out_neuron.id]

            if conn.enabled:
                opacity = (int(255 * conn.weight), int(255 * conn.weight), int(255 * conn.weight))
                Connection(start_neuron.pos, out_neuron.pos, color=opacity).draw(self.surface)

    def get_surface(self):
        self.visualize()
        return self.surface
                
