
import matplotlib.pyplot as plt
import os

"""
This program will generate graphs and calculations using data from 2 csv files, including:
1) The average highs per month
2) The extreme highs per month
3) The comparison of extreme highs and lows
4) The extreme precipitation per month
5) Print calculations:
    a) The month with largest range of temperatures
    b) The month with the highest value
    c) The month with the lowest value
    d) The amount of months where temperatures were in the hundreds
"""

# ---------------TODO--------------
# Read in the csv files

def read_file(filename):
    full_path = os.path.join("docs", filename)
    data_lists = []
    try:
        with open(full_path, "r") as f:
            for index, line in enumerate(f):
                # Skip the header line
                if index == 0:
                    continue
                else:
            # For each line: split the line by commas, strip the whitespace, store the data in lists
                    line = line.strip()
                    data = line.split(",")
                    data_lists.append(data)
    except FileNotFoundError:
        return "file not found"
    return data_lists

# convert to int or float when needed

# make separate lists for months, temp, and rainfall/snowfall
def separate_lists(data_lists):
    months = []
    average_high = []
    average_low = []
    precipitation = []
    for row in data_lists:
        months.append(row[0])
        average_high.append(int(row[1]))
        average_low.append(int(row[2]))
        precipitation.append(float(row[3]))
    return data_lists, months, average_high, average_low, precipitation



# ---------------TODO-----------------
# create a tuple of colors
bar_colors = ("#3c096c", "#5a189a", "#7400b8", "#6930c3", "#5e60ce", "#5390d9", "#4ea8de", "#48bfe3",
                  "#56cfe1", "#64dfdf", "#72efdd", "#80ffdb")

# --------------TODO ------------------
# choose a chart
def average_csv():
    # include: a title, x-axis and y-axis labels, tick labels for the months, a grid, color choices from the tuple
    x_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_coords = a_high
    plt.title("Average Highs of Flatbush")
    plt.bar(x_coords, y_coords, color=bar_colors)
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Temperature(F)")
    plt.xticks(ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels=["Jan", "Feb", "Ma", "Apr","May", "Jun",
                                                                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.show()

    # print to the console:
    # the month with the highest value shown in your graph
    # the month with the lowest value shown in your graph
    print("----------------------AVERAGE TEMPERATURES---------------------------")
    print("The month with the highest value on this graph is July")
    print("The month with the lowest value on this graph is December")
    above_number(a_high,80)


# -------------TODO -----------------
# make a second graph using flatbush extremes csv
def extreme_csv():
    x_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_coords = e_high
    plt.title("Extreme Highs of Flatbush")
    plt.bar(x_coords, y_coords, color=bar_colors)
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Temperature(F)")
    plt.xticks(ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels=["Jan", "Feb", "Ma", "Apr","May", "Jun",
                                                                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.show()

    print("-----------------------EXTREME TEMPERATURES---------------")
    print("The month with the highest extreme temperature is July.")
    print("The month with the lowest extreme value is January.")
    above_number(e_high,100)

# compare record highs and lows
def compare_records_extremes():
    x_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_e_high = e_high   # The y values for extreme highs
    y_e_low = e_low     # The y values for extreme lows
    plt.title("Comparing Record Highs and Lows")
    plt.plot(x_coords, y_e_high, label="Extreme Highs")
    plt.plot(x_coords, y_e_low, label="Extreme Lows")
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Temperature(F)")
    plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels=["Jan", "Feb", "Ma", "Apr", "May", "Jun",
                                                                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    plt.show()

# choose a different graph to plot snowfall by month
def extreme_precipitation():
    x_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_coords = e_precipitation
    plt.title("Snowfall by Month")
    plt.bar(x_coords, y_coords, color = bar_colors)
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Snowfall(inches)")
    plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels=["Jan", "Feb", "Ma", "Apr", "May", "Jun",
                                                                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.show()

    print("------------------SNOWFALL ANALYSIS--------------")
    print("The month with the highest snowfall was January.")
    print("The months with no snowfall were May, June, July, August, September, and October.")
    total = 0

    for prec in e_precipitation:
        total += prec

    print(f"The total snowfall was {total} \n")

# calculate which month has the largest temp range
def calculate_ranges():
    month = None
    highest = 0
    lowest = 1000
    total = 0
    count = 0
    for index, month in enumerate(months):
        calc = e_high[index] - e_low[index]
        total += calc
        count += 1
        if calc > highest:
            highest = calc
            high_month = months[index]
        if calc < lowest:
            lowest = calc
            low_month = months[index]
    average = total / count
    print(" ------------------TEMPERATURE RANGES-------------------")
    print(f" The month with the largest temperature range was {high_month} with a range of {highest}.")
    print(f" The month with the lowest temperature range was {low_month} with a range of {lowest}.")
    print(f"The average temperature range was {average} \n")


# ---------------TODO ------------------
# print to the console:
# the month with the highest value shown in your graph
# the month with the lowest value shown in your graph

# one additional numeric summary ( average, total, or difference)
def above_number(temperatures, number):
    count= 0
    for temp in temperatures:
        if temp >= number:
            count+= 1
    print(f"The amount of months with temperatures over {number} degrees was {count} \n")
    return count


# --------------TODO--------------------
# call functions with arguments

def main():

    # Plot graphs
    average_csv()
    extreme_csv()
    compare_records_extremes()
    extreme_precipitation()

    # calculate which month had the largest range
    calculate_ranges()

# Call separate lists and unpack tuples into global variables
# e refers to extremes, a refers to averages
average_lists = read_file("weather_data_flatbush.csv")
average_lists, months, a_high, a_low, a_precipitation = separate_lists(average_lists)
extreme_lists = read_file("flatbush_extremes.csv")
extreme_lists, months, e_high, e_low, e_precipitation = separate_lists(extreme_lists)

# call main
if __name__ == "__main__":
    main()


