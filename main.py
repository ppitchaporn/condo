import pandas as pd
from rapidfuzz import process, fuzz

# Load the Excel files
cleaned_data_path = r'D:\NIDA\5002\midterm_project\cleaned_for_model1.xlsx'
tambon_data_path = r'D:\NIDA\5002\midterm_project\ThepExcel-Thailand-Tambon.xlsx'

# Read the required sheets and tables
cleaned_df = pd.read_excel(cleaned_data_path, sheet_name='Sheet1')
tambon_df = pd.read_excel(tambon_data_path, sheet_name='TambonDatabase')

# Extract the relevant columns for mapping
relevant_columns = ['DistrictThai', 'DistrictEng', 'DistrictThaiShort', 'DistrictEngShort', 'PostCodeMain', 'ProvinceThai', 'ProvinceEng']
mapping_df = tambon_df[relevant_columns]

# Preprocess district and province names for better matching using .loc to avoid the SettingWithCopyWarning
mapping_df.loc[:, 'DistrictThai'] = mapping_df['DistrictThai'].str.strip().str.lower()
mapping_df.loc[:, 'ProvinceThai'] = mapping_df['ProvinceThai'].str.strip().str.lower()

# Function to extract and match district and province from address
def extract_and_match_district(address):
    parts = [part.strip().lower() for part in address.split(',')]
    district = parts[-2] if len(parts) > 1 else ""
    province = parts[-1] if len(parts) > 0 else ""
    match_row = mapping_df[(mapping_df['DistrictThai'] == district) & (mapping_df['ProvinceThai'] == province)]
    if not match_row.empty:
        return match_row.iloc[0]['DistrictThai']
    result = process.extractOne(query=district, choices=mapping_df['DistrictThai'], scorer=fuzz.token_sort_ratio)
    if result:
        match, score, _ = result
        return match if score >= 70 else None
    return None

# Extract the condo name from 'rent_cd_name' and add it as 'Condo_Name'
def extract_condo_name(rent_cd_name):
    return rent_cd_name.split(':')[0].strip() if ':' in rent_cd_name else rent_cd_name.strip()

# Apply the extraction function to create the 'Condo_Name' column
cleaned_df['Condo_Name'] = cleaned_df['rent_cd_name'].apply(extract_condo_name)

# Apply the extraction and matching to each row in 'rent_cd_address'
cleaned_df['MatchedDistrictThai'] = cleaned_df['rent_cd_address'].apply(extract_and_match_district)

# Filter out unreasonable rent prices using the IQR method
q1 = cleaned_df['rent_cd_price'].quantile(0.25)
q3 = cleaned_df['rent_cd_price'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Keep only listings within the reasonable price range
filtered_df = cleaned_df[(cleaned_df['rent_cd_price'] >= lower_bound) & (cleaned_df['rent_cd_price'] <= upper_bound)]

# Merge the matched district information back with the mapping dataframe to get postcode and other details
merged_df = filtered_df.merge(
    mapping_df,
    left_on='MatchedDistrictThai',
    right_on='DistrictThai',
    how='left'
)

# Drop the unnecessary columns before saving
merged_df = merged_df.drop(columns=['MatchedDistrictThai', 'DistrictThai', 'DistrictEng'])

# Save the filtered and merged result to a new Excel file
output_path = r'D:\NIDA\5002\midterm_project\Condo_Data_PostCode_Filtered.xlsx'
merged_df.to_excel(output_path, index=False)

print(f"Filtered and merged data saved to {output_path}")
