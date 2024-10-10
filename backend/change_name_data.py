from pathlib import Path
from shutil import copytree, rmtree
# (explain what this code does(Lab)): This code imports a library that allows for the access of the directories of the lab
#pathlib and shutil are libraries for editing directories (files , folders etc)
raw_data_path = Path(__file__).parent / "raw_data"
cleaned_data_path = Path(__file__).parent / "cleaned_data"
# we have the paths of 2 of our designated work folders, one has the raw data and the other we are preparing for
# the cleaned data that we will work with 
if cleaned_data_path.is_dir():
    rmtree(cleaned_data_path)
# deletes the directory of the cleaned data folder , to ensure the code runs for everyone same way
cleaned_data_path.mkdir(parents=True, exist_ok=True)
# Making the directory for the cleaned data folder after removing its contents
for folder in raw_data_path.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder, cleaned_data_path / new_name)

# takes basically every folder in raw data and splits its first name which is what we want and gives it as a name
#to the cleaned data folder