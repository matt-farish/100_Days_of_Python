# Day 25 of Udemy's 100 Days of Python programming course
import csv
import pandas
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# data_list = data["temp"].to_list()

# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 1.8 + 32)

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count  = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Colour" : ["Gray", "Cinammon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")