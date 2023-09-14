import pandas as pd
from sklearn.model_selection import train_test_split

# Define the path to your CSV file containing the dataset
csv_file_path = 'speech_to_speech_dataset.csv'  # Replace with the actual file path

# Load the dataset into a Pandas DataFrame
dataset = pd.read_csv(csv_file_path)

# Split the dataset into training, validation, and testing sets
# Using train_test_split from scikit-learn for proper random splitting
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

train_dataset, test_val_dataset = train_test_split(dataset, test_size=(1 - train_ratio))
val_dataset, test_dataset = train_test_split(test_val_dataset, test_size=test_ratio / (test_ratio + val_ratio))

# Verify the sizes of the splits
print(f"Number of training samples: {len(train_dataset)}")
print(f"Number of validation samples: {len(val_dataset)}")
print(f"Number of testing samples: {len(test_dataset)}")
