from database import Database
from constants import CLEANED_DATA_PATH, DATABASE_PATH
# we are basically taking the database as a component to work with by importing it
# We are also taking the paths we just used in the renaming to work with as well
def ingest_csv_data_to_duckdb():
    """ingesting the cleaned csv data to duckdb"""
    translation_table = str.maketrans({"å": "a", "ä": "a", "ö": "o" , "O" : "o", "I" : "i"})
    # this code removes the rune symbols on the csv files
    for directory_path in CLEANED_DATA_PATH.glob("*"):
        #runs through all of the directories inside cleaned data folder
        schema_name = directory_path.name.lower().translate(translation_table)
        # takes the renamed name of the folder as a variable
        for csv_path in directory_path.glob("*"):
            table_name = csv_path.name.lower().split(".")[0].translate(translation_table)
            #takes the renamed/edited names of the csv files
            with Database(DATABASE_PATH) as db:
                #creates the schema for ingesting in database
                db.query(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
                db.query(
                    f"""
                        CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS
                        SELECT * FROM read_csv_auto('{csv_path}');
                        """
                )

if __name__ == '__main__':
    ingest_csv_data_to_duckdb()