import pandas as pd

# Read the input CSV file
df = pd.read_csv('dummyText1.csv')

# Combine 'Dataset Description' and 'Tags/Keywords' into 'Overview'
df['Overview'] = df['Dataset Description'] + ', ' + df['Tags/Keywords']

# Drop the original 'Dataset Description' and 'Tags/Keywords' columns
df.drop(['Dataset Description', 'Tags/Keywords'], axis=1, inplace=True)

# Save the modified DataFrame to a new CSV file
df.to_csv('output.csv', index=False)
