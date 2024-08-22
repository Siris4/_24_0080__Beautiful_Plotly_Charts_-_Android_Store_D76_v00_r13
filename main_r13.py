import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Clean the 'Price' column by removing the $ sign and converting to float
df['Price'] = df['Price'].str.replace('$', '').astype(float)

# Clean the 'Installs' column by removing commas and plus signs, then convert to integer
df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '').astype(int)

# Add a new column 'Revenue_Estimate' to the DataFrame
df['Revenue_Estimate'] = df['Price'] * df['Installs']

# Sort the DataFrame by 'Revenue_Estimate' in descending order to find the top 10 apps by revenue estimate
top_revenue_apps = df.sort_values(by='Revenue_Estimate', ascending=False).head(10)

# Display the top 10 apps by Revenue_Estimate
print(top_revenue_apps[['App', 'Price', 'Installs', 'Revenue_Estimate']])
