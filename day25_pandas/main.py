import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['score'])
# score_list = data['score'].to_list()
# print(score_list)
# csv = data.to_dict()
# print(csv)
# print('*'*50)
# print(data[data['score']==90])
# print(data['score'].max())
# print(data['score'].mean())

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data.groupby('Primary Fur Color').size())