from pipelines.WB.steps.download import download_all_data
from pipelines.WB.steps.unzip import parallel_unzip
from pipelines.WB.steps.merge import merge_files
from pipelines.WB.steps.cleanup import cleanup
from pipelines.utils.upload import upload_files_to_s3
import os


def main():
    # Get the absolute path of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change the working directory to the script directory
    os.chdir(script_dir)

    # Run the ETL process
    download_all_data()
    parallel_unzip()
    merge_files()
    cleanup()
    file_list = ["./data/Metadata_Country.parquet", "./data/Metadata_Indicator.parquet", "./data/Indicator.parquet"]
    upload_files_to_s3(file_list)


if __name__ == "__main__":
    main()
