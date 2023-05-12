import os
import glob


def cleanup(directory_path="./data"):
    file_types_to_remove = [
        "Metadata_Indicator_API_*",
        "Metadata_Country_API_*",
        "API_*",
        "*.zip",
    ]
    for file_type in file_types_to_remove:
        for file in glob.glob(f"{directory_path}/{file_type}"):
            os.remove(file)
