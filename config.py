FLAP_THRESHOLD = 0.5

POPULATION = 100

SURVIVORS = 10

# Randomizing
WEIGHT_SMALL_MUTATION_PROB = 0.7
WEIGHT_BIG_MUTATION_PROB = 0.3

# Neural network
INPUT_NEURONS = 5 # Bird.jumping / Bird.y / Pipes.x / TopPipe.y / BotPipe.y
HIDDENS = [6,5,4]
OUTPUT_NEURONS = 1
TOPOLOGY = [INPUT_NEURONS] + HIDDENS + [OUTPUT_NEURONS]
