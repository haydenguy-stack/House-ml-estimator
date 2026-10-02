from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

data =  {
    'Square_feet': [1500, 2200, 1100, 3500, 1800],
    'Bedrooms': [3, 4, 2, 5, 3],
    'Bathrooms': [2.0, 2.5, 1.0, 4.5, 2.0],
    'Stories': [1, 2, 1, 2, 1],
    'Year': [2005, 2018, 1985, 2022, 1998],
    'Garage': [True, True, False, True, True],
    'Price': [285000, 420000, 175000, 850000, 310000]
}
df = pd.DataFrame(data)
df["Garage"] = df["Garage"].astype(int)
X = df[["Square_feet", "Bedrooms" , "Bathrooms", "Stories", "Year", "Garage"]]
Y = df["Price"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size= .2, random_state=30)

model = RandomForestRegressor(n_estimators=100, random_state= 30)

model.fit(x_train, y_train)

sq_ft = int(input("Size of the home: "))
Bedroom =  float(input("amount of bedrooms: "))
bathroom = float(input("number of bathrooms: "))
floors = int(input("number of stories:"))
year = int(input("built: "))
garage = input("Garage? (yes/no): ").strip().lower()
user_garage = 1 if garage in ["yes", "YES", "y"] else 0

house = {
    'Square_feet': [sq_ft],
    'Bedrooms': [Bedroom],
    'Bathrooms': [bathroom],
    'Stories': [floors],
    'Year': [year],
    'Garage': [user_garage],
}
new_house = pd.DataFrame(house)
predict = model.predict(new_house)
print(predict)






