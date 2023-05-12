import os
import zipfile
from concurrent.futures import ThreadPoolExecutor
import multiprocessing


def extract_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall("./data")


def parallel_unzip(directory_path="./data"):
    zip_files = [f for f in os.listdir(directory_path) if f.endswith(".zip")]
    num_cores = multiprocessing.cpu_count()
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        executor.map(extract_zip, [os.path.join(directory_path, f) for f in zip_files])
