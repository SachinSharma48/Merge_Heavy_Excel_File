import pandas as pd
file_path = 'C:/Users/Stockyana.com/Desktop/Data1.csv'
df = pd.read_csv(file_path)
filtered_df = df[df['Country '] == 'India']

new_file_path = 'C:/Users/Stockyana.com/Desktop/Data1.csv'
filtered_df.to_csv(new_file_path, index=False)

print('Filtered data saved to', new_file_path)

#  2nd Step for Merging


1_df = pd.read_csv('C:/Users/Stockyana.com/Desktop/Data1.csv')
2_df = pd.read_excel('C:/Users/Stockyana.com/Desktop/Data2.xlsx', sheet_name='Stockyana')
1_df['Name'] = 1_df['Name'].str.lower()
2_df['Name'] = mapping_df['Name'].str.lower()
2_df = pd.merge(1_df, 2_df, left_on='Name', right_on='Name', how='left')
2_df.drop_duplicates(subset='Name', keep='first', inplace=True)
result_df = 2_df[['ID', 'Name']]
1_df = pd.merge(1_df, result_df, on='Name', how='left')
1_df['Name'] = 1_df['Name'].str.capitalize()
print(1_df)

1_df.drop_duplicates(inplace=True)
1_df = 1_df[1_df['ID'].notnull()]
1_df.rename(columns={'ID': 'Cust_ID'}, inplace=True)
1_df.to_csv('C:/Users/Stockyana.com/Desktop/Data1', index=False, columns=['Name', 'ID', 'Mobile', 'Email_id'])
print("Done.")
