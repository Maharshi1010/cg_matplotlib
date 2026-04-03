import pandas as pd

data = {
    'Name': ['Maharshi', 'Sanali', 'Nakul', ],
    'Age': [21, 19, 20],
    'City': ['Nagpur', 'Mahabaleshwar', 'Pune']
}

myData = pd.DataFrame(data)
print(myData)