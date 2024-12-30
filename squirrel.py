import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240617.csv")

grey_squirrels = len(data[data.Primary_Fur_Color == "Gray"])
cinnamon_squirrels = len(data[data.Primary_Fur_Color == "Cinnamon"])
black_squirrels = len(data[data.Primary_Fur_Color == "Black"])


data_dict = {
    "Fur Colour": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_count.csv")