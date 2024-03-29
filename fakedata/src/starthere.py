#!/usr/bin/python

from datafiles import service_and_equipment
from my_project_utils import random_generator

start = service_and_equipment.FileGeneration()
rn = random_generator.RandomCustom()

# The seed for the random generator
rn.random_seed(3)
# The number of networks that are wanted in the output
numberOfNetworks = 350  # sys.argv[0]
start.file_generator_iterations(numberOfNetworks)
# those network can have address_class of type b, or c as
# type a take too long to fulfill. (Please see comments on
# src/datafiles/service_and_equipment.py:73)
