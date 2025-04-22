import os
import shutil

# Define paths
source_dir = 'data/train'
cat_dir = os.path.join(source_dir, "cats")
dog_dir = os.path.join(source_dir, "dogs")

# Create directories if they don't exist
os.makedirs(cat_dir, exist_ok=True)
os.makedirs(dog_dir, exist_ok=True)

# Loop through files in the source directory
for filename in os.listdir(source_dir):
    # Skip the "cats" and "dogs" directories
    if filename in ["cats", "dogs"]:
        continue
    if filename.startswith("cat"):
        # Move cat images
        shutil.move(os.path.join(source_dir, filename), os.path.join(cat_dir, filename))
    elif filename.startswith("dog"):
        # Move dog images
        shutil.move(os.path.join(source_dir, filename), os.path.join(dog_dir, filename))

# Print confirmation
print(f"Organized dataset into {cat_dir} and {dog_dir}")