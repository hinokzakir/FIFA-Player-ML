import pandas as pd

input_csv = 'data/male_players_original.csv'  # Original file path
output_csv = 'data/male_players_cleaned.csv'  # Output file path

# List the columns you want to keep
columns_to_keep = ['player_id', 'overall', 'age', 'player_positions', 'skill_moves', 'work_rate', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
# Read the CSV
df = pd.read_csv(input_csv)

# Keep only the specified columns
df_filtered = df[columns_to_keep]

# Save the filtered DataFrame to a new CSV
df_filtered.to_csv(output_csv, index=False)