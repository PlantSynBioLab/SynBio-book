import pandas as pd
import os

# Load the spreadsheet
df = pd.read_excel('supplements/YTK_Parts.xlsx')

# Clean column names just in case
df.columns = df.columns.str.strip()


# Path to the folder with .gb files
plasmid_dir = 'supplements/YTK_plasmids'

# Loop through each row and rename files
for _, row in df.iterrows():
    plasmid_name = row['Plasmid Name'].strip()
    part_type = str(row['Part Type']).strip()
    part_desc = row['Part Description'].strip().replace(' ', '_')

    old_name = os.path.join(plasmid_dir, f"{plasmid_name}.gb")
    new_name = os.path.join(plasmid_dir, f"{plasmid_name}_{part_type}_{part_desc}.gb")
    
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")

# Load the spreadsheet
df = pd.read_excel('supplements/MYT_Parts_Data.xlsx')

# Clean column names just in case
df.columns = df.columns.str.strip()


# Path to the folder with .gb files
plasmid_dir = 'supplements/MYT_Plasmids'

# Loop through each row and rename files
for _, row in df.iterrows():
    plasmid_name = row['Plasmid Name'].strip()
    part_type = str(row['Part Type']).strip()
    part_desc = row['Plasmid Description'].strip().replace(' ', '_')

    old_name = os.path.join(plasmid_dir, f"{plasmid_name}.gb")
    new_name = os.path.join(plasmid_dir, f"{plasmid_name}_{part_type}_{part_desc}.gb")
    
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")

        
        

