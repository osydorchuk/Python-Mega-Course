def get_average():
    with open("../files/temperature.txt", 'r') as file:
        temperature_data = file.readlines()
    temperature_values = temperature_data[1:]
    temperature_values = [float(i) for i in temperature_values]

    average_local = sum(temperature_values)/len(temperature_values)
    return average_local


average = get_average()
print(average)