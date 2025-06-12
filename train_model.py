import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("data/cloud_sales_forecasting_3lakh.csv")

# Convert 'Date' to datetime and extract features
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df.drop('Date', axis=1, inplace=True)

# Encode categorical variables
le_product = LabelEncoder()
le_category = LabelEncoder()
le_region = LabelEncoder()

df['Product_ID'] = le_product.fit_transform(df['Product_ID'])
df['Category'] = le_category.fit_transform(df['Category'])
df['Region'] = le_region.fit_transform(df['Region'])

# Save the encoders
joblib.dump(le_product, 'le_product.pkl')
joblib.dump(le_category, 'le_category.pkl')
joblib.dump(le_region, 'le_region.pkl')

# Features and target
X = df.drop('Sales_Revenue ($)', axis=1)
y = df['Sales_Revenue ($)']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Save the model
joblib.dump(model, 'sales_forecasting_model.pkl')
print("Linear Regression model saved to sales_forecasting_model.pkl")
