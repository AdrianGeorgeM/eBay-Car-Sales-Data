import pandas as pd
import numpy as np

import re

filepath = "autos.csv"
autos = pd.read_csv(filepath,encoding='latin-1')
# print("Number of rows and columns:", autos.shape)
# print("Column names:", autos.columns)
# print("Data types:\n", autos.dtypes)

# print("Number of rows and columns:", autos.shape)
# print("Column names:")
# for column in autos.columns:
#     print(column)



# Function to convert camelCase to snake_case
def camel_to_snake(name):
    """
    Convert a camelCase string to snake_case.
    """
    # Insert an underscore before any uppercase letter followed by a lowercase letter, then convert to lowercase.
    snake_case_name = re.sub('([a-z])([A-Z])', r'\1_\2', name).lower()
    return snake_case_name

# The specific column renames
mapping_dict = {
    "yearOfRegistration": "registration_year",
    "monthOfRegistration": "registration_month",
    "notRepairedDamage": "unrepaired_damage",
    "dateCreated": "ad_created"  
}

# Assuming 'autos' is your DataFrame
new_columns = []

for columns in autos.columns:
    if columns in mapping_dict:
        new_columns.append(mapping_dict[columns])
    else:
        new_columns.append(camel_to_snake(columns))

autos.columns = new_columns

autos.describe(include='all')

## Observations from Descriptive Statistics

# - **Columns to Drop**: Identify any columns that predominantly contain a single value, which are not useful for analysis.
# - **Further Investigation**: Note the columns that require more detailed examination.
# - **Numeric as Text**: Identify columns where numeric data is stored as text, necessitating cleaning and conversion.

autos['name'].value_counts().head()

## Additional Observations

# - Detail any noteworthy findings from the investigation of specific columns.

# autos.describe(include='all')

autos = autos.drop(["seller","offer_type","nr_of_pictures"], axis=1)

autos["price"] = autos["price"].str.replace("$","").str.replace(",","").astype(int)

# autos["odometer"] = (autos["odometer"]
#                              .str.replace("km","")
#                              .str.replace(",","")
#                              .astype(int)
#                              )

autos.rename({"odometer": "odometer_km"}, axis=1, inplace=True)
autos[['price', 'odometer_km']].head(10)

# %%
autos.iloc[:, :7].head()

# %%
# autos["price"].value_counts().sort_index(ascending=True).head(20)
# Filter the DataFrame for rows where the price is 2
# rows_with_price_2 = autos[autos["price"] == 2]
# rows_with_specific_name = autos[autos["name"] == "Volkswagen_Golf_1.6_United"]

# Display these rows
# print(rows_with_specific_name[["name","vehicle_type"]])
# print(rows_with_price_2[["name","vehicle_type"]])

# %%
# First, get the value counts and sort them
registration_year = autos["registration_year"].value_counts() 

# gearbox = autos["gearbox"].value_counts()
# Then, filter for years 2004 or earlier
registration_year = registration_year[registration_year.index <= 2004]

print(registration_year)
# print(gearbox)



