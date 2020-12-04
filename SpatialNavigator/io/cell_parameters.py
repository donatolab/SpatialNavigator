# define place cells and set parameters
cell_1 = {'is_place_cell': True, 'centroid_position': 30, 'size_firing_field': 34, 'reliability': 0.75}
cell_2 = {'is_place_cell': True, 'centroid_position': 55, 'size_firing_field': 41, 'reliability': 0.55}
cell_3 = {'is_place_cell': True, 'centroid_position': 110, 'size_firing_field': 25, 'reliability': 0.90}

# define non-place cells
cell_4 = {'is_place_cell': False}
cell_5 = {'is_place_cell': False}

cells = [cell_1, cell_4, cell_5, cell_2, cell_3]