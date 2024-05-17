import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

df = pd.read_excel(r'C:\Users\karth\Desktop\Train_Emission_Sample.xlsx')

df = pd.get_dummies(df, columns=['Vehicle_Type'], drop_first=True)

X = df[['Mileage(km/L)', 'Distance(km)', 'Vehicle_Type_4']]
y = df['CO2_Emissions(g/km)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_regressor = RandomForestRegressor(n_estimators=200, random_state=42)
rf_regressor.fit(X_train, y_train)

y_pred = rf_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

joblib.dump(rf_regressor, 'newpicklefile1.pkl')
