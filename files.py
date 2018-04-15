# Precondition for all functions in this module: each line of the temperature
# file contains the average monthly temperatures for a year (separated
# by spaces) starting with January.  The file must also have 3 header lines.

def open_temperature_file(filename):
    """(str) -> file open for reading

    Open the file named filename, read past the three-line header, and 
    return the open file.
    """
    open_file = open(filename, 'r')
    open_file.readline()
    open_file.readline()
    open_file.readline()
    return open_file    


def avg_temp_march(f):
    """(file open for reading) -> float

    Return the average temperature for the month of March
    over all years in f.
    """
    nested_temperature_list = []
    item = 0
    jtem = 0
    sum_march = 0
    march_temperature = []
    for line in f:
        temperature_list = line.split()
        nested_temperature_list.append(temperature_list)
    for item in range(len(nested_temperature_list)):
        march_temperature.append(nested_temperature_list[item][2])
        item += 1
    for jtem in range(len(march_temperature)):
        if march_temperature[jtem] != '':
            sum_march += float(march_temperature[jtem])
            jtem += 1
    return (sum_march / len(march_temperature))
                                    
            


def avg_temp(f, mo):
    """(file open for reading, int) -> float

    Return the average temperature for month mo over all
    years in f. mo is an integer between 0 and 11, representing
    January to December, respectively.
    """
    nested_temperature_list = []
    item = 0
    jtem = 0
    sum_march = 0
    march_temperature = []
    for line in f:
        temperature_list = line.split()
        nested_temperature_list.append(temperature_list)


def higher_avg_temp(filename, month1, month2):
    """(str, int, int) -> int

    Return either month1 or month2 (integers representing months in the
    range 0 to 11), whichever has the higher average temperature over
    all years in the file at filename.  If the months have the 
    same average temperature, then return -1.
    """


def three_highest_temps(f):
    """(file open for reading) -> list of float

    Return the three highest temperatures, in descending order, 
    over all months and years in f.
    """


def below_freezing(f):
    """(file open for reading) -> list of float
    
    Return, in ascending order, all temperatures below freezing 
    (32 degrees Fahrenheit), for all temperature data in f. 
    Include any duplicates that occur.
    """