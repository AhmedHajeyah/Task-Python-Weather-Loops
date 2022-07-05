# printer(elements)
# - Accepts a list
# - Prints every element of the list

from readline import append_history_file
from xml.dom.minidom import Element


# elements = [1, 2, 3, 4, 5]

def printer(elements):
    # Your code here
    for element in elements:
        print(element)
    
# printer(elements)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)

# temperatures_list = [100,120,99]

def to_celsius(temperatures):
    # Your code here
    ctemp=[]
    for temp in temperatures:
        ctemp.append((temp-32)*5/9)
    print(ctemp)
    return ctemp

# to_celsius(temperatures_list)

# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold


# temperatures_list = [102,120,99,103,120]
# threshold_temp = 100

def hottest_days(temperatures, threshold):
    # Your code here
    temp=[]
    temp_above_threshold = []
    for temp in temperatures:
        if temp >= threshold:
            print(temp)
            temp_above_threshold.append(temp)
    return temp_above_threshold

#hottest_days(temperatures_list, threshold_temp)
     


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions

temperatures_list = [102,120,99,103,120]
threshold_temp = 100

def print_hottest_days(temperatures, threshhold):
    # Your code here
    for tempa in temperatures:
        print(tempa)
    to_celsius(temperatures)
    hottest_days(temperatures, threshhold)

print_hottest_days(temperatures_list, threshold_temp)

