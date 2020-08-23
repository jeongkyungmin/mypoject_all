friend_dict_list = [{'name': 'John', 'midterm': 95, 'final': 85},
         {'name': 'Jenny', 'midterm': 85, 'final': 80},
         {'name': 'Nate', 'midterm': 10, 'final': 30}]
df = pd.DataFrame(friend_dict_list, columns = ['name', 'midterm', 'final'])
print(df)

rades = []

for row in df['average']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    elif row >= 70:
        grades.append('C')
    else:
        grades.append('F')

df['grade'] = grades