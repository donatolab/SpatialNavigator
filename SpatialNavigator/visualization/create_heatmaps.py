import matplotlib.pyplot as plt


# for each cell, calculate the percentage of time at which an event occurred at each position
def calc_avg_activity():
    # for each position, calculate the average activity of each cell
    averaged_data = tracking_data.groupy('position').mean()
    sorted_data = averaged_data.sort_values(by=['position'])
    return sorted_data

# create heatmap
def create_heatmap(sorted_data):
    fig, ax = plt.subplots()
    heatmap = ax.pcolormesh(sorted_data)
    fig.colorbar(heatmap, ax)
    plt.show()