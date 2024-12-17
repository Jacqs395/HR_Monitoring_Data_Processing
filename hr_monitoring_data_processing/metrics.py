import statistics 

def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    # create empty list to store maximum value from every window
    # create For Loop to get maximum data, then append to the empty list
    maximum = []
    for y in range(0, len(data), n):
        window = data[y: y + n]
        maximum.append(max(window))
    return maximum


def window_average(data: list, n: int) -> list:
# create empty list to store window averages
# create For Loop to calculate average from data list, with a window size of 'n'
# calculate average, using averages formula
# append average to empty list, round to 2 places

    average_list = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        average = sum(window) / len(window)
        average_list.append(round(average, 2))
    return average_list
    

def window_stddev(data: list, n: int) -> list:
    if data == []:
        return data
    standard_deviation = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        if len(window) == 1:
            continue
        std_dev = statistics.stdev(window)
        standard_deviation.append(round(std_dev,2))
    return standard_deviation

    
    






