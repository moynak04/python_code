import csv

with open(r"C:\python_codes\.vscode\day25\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)