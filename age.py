# data['Год Рождения'] is imported as 'object' so we must convert it to float / int
data['Год Рождения'] = data['Год Рождения'].convert_objects(convert_numeric=True)
data['Год Рождения']

# data['Отметка времени'] has format like '13.10.2015 17:50:14' so we must extract 'year' 

data['Отметка времени'] = pd.to_datetime(data['Отметка времени'])
data['year'] = data['Отметка времени'].apply(lambda x: x.year)

# now we get 'age'
data['age'] = data['year'] - data['Год Рождения']
data['age']
