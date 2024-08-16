import argparse
import math

# Init argument parser
argument_parser = argparse.ArgumentParser()

# Adding optional arguments
argument_parser.add_argument("-f", "--farm_size", default = "123", help = "The size of your farm in tiles")
argument_parser.add_argument("-o", "--optimal", default = "100", help = "The expected tiles per farmer. A 100 is a good value for most players")

# Parse arguments
arguments = argument_parser.parse_args()
optimal_tiles_per_farmer = int(arguments.optimal)
total_farm_size = int(arguments.farm_size)

# Calculate the amount of farmers needed
print("Calculating with farm size: " + str(total_farm_size) + " and optimal tiles per farmer: " + str(optimal_tiles_per_farmer))
farmer_count = math.ceil(total_farm_size / optimal_tiles_per_farmer)
print("You need at least " + str(farmer_count) + " farmers")
