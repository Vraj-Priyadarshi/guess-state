# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp = int(row[1])
# #             temperatures.append(temp)
# #     print(temperatures)
# #
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # maximum = data.temp.max()
# # print(data[data.temp == maximum])
# monday = data[data.day == "Monday"]
# faranheith = (monday.temp[0]* (9/5)) + 32
# print(faranheith)
