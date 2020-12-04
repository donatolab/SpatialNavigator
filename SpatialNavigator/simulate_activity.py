from .io import cell_parameters
from .io import tracking_data

# calculate a place cell's firing probability for a given position in the environment
def calc_probability (position, size, reliability, position):

# determine whether a place cell will fire based upon probability
...

# determine whether a non-place cell will fire based upon probability
...

# determine whether a cell is active or not
def sim_activity (cell, position):
    if cell['is_place_cell']:
        activity = calc_probability(...)
    else:
        activity = rand_activity
return activity

def sim_cells (tracking_data, cell_parameters):
    for row in tracking_data:
        for cell in cells:
            sim_activity(cell, position)
            #put activity in column
return ...