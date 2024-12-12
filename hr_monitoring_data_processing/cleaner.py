def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    if len(data) == 0:
        return data
    
    new_data = []
    for element in data:
        #check if my element is a digit (considering \n)
        #if it is, append to my new list
        element = element.strip()
        if element.isdigit():
            new_data.append(int(element))
        else: 
            element = element
    return new_data
in_data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]
print(filter_nondigits(in_data))


def filter_outliers(data: list) -> list:
    pass
