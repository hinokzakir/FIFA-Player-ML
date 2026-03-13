import pandas as pd

input_csv = 'data/male_players_original.csv'  # Original file path
output_csv = 'data/male_players_cleaned.csv'  # Output file path

# List the columns you want to keep
columns_to_keep = ['player_id', 'overall', 'age', 'player_positions', 'skill_moves', 'work_rate', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
# Read the CSV
df = pd.read_csv(input_csv)

# Keep only the specified columns
df_filtered = df[columns_to_keep]

# remove rows with only "GK" as position
df_filtered = df_filtered[df_filtered['player_positions'] != 'GK']

# Convert work_rate strings like "high/medium" into numeric features.
# We split into attacking and defensive rates and map low/medium/high to 1/2/3.
work_rate_map = {'low': 1, 'medium': 2, 'high': 3}
work_rate_parts = (
	df_filtered['work_rate']
	.astype(str)
	.str.strip()
	.str.lower()
	.str.split('/', expand=True)
)

df_filtered['attacking_work_rate'] = work_rate_parts[0].map(work_rate_map)
df_filtered['defensive_work_rate'] = work_rate_parts[1].map(work_rate_map)

# Default unknown/missing values to medium (2), then cast to int.
df_filtered['attacking_work_rate'] = df_filtered['attacking_work_rate'].fillna(2).astype(int)
df_filtered['defensive_work_rate'] = df_filtered['defensive_work_rate'].fillna(2).astype(int)

# Keep only numeric versions for modeling.
df_filtered = df_filtered.drop(columns=['work_rate'])

# Save the filtered DataFrame to a new CSV
df_filtered.to_csv(output_csv, index=False)