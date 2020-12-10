import pandas as pd
import numpy as np

import random
from scipy.stats import norm

from .io.cell_parameters import cells


# create dataframe from csv file with tracking data
tracking_data = pd.read_csv('io/tracking_data.csv')


# add simulated data to the dataframe with tracking data
def sim_data():
    # simulate cell activity
    simulated_data = sim_cells()
    data_array = np.asarray(simulated_data)
    for i in range(len(cells)):
        # create the name of the column
        column_name = f'cell_{i}'
        # assign the activity for one cell into a new column in the dataframe with tracking data
        tracking_data[column_name] = data_array[:, i]
    return tracking_data


# simulate active cells during spatial navigation
def sim_cells():
    simulated_data = []
    for row in tracking_data.itertuples():
        position = row['position']
        activity_cells = []
        for cell in cells:
            activity = sim_activity(cell, position)
            activity_cells.append(activity)
        simulated_data.append(activity_cells)
    return simulated_data


# for the current position, determine whether a cell fires or not
def sim_activity(cell, position):
    if cell['is_place_cell']:
        random_probability = random.uniform(0, 100)
        if random_probability < calc_probability(cell, position):
            activity = 1
        else: activity = 0
    else:
        activity = random.getrandbits(1)
    return activity


# for the current position, calculate the firing probability of a place cell
def calc_probability(cell, position):
    dist_from_centroid = abs(cell['centroid_position'] - position)
    fire_field_radius = cell['size_firing_field'] / 2
    if dist_from_centroid <= fire_field_radius:
        sigma = cell['size_firing_field'] / 6
        gaussian_max = norm.pdf(0)
        scale_y_axis = gaussian_max * cell['reliability']
        probability = norm.pdf(dist_from_centroid, loc=cell['centroid_position'], scale=sigma) / scale_y_axis
    else:
        probability = 0
    return probability



