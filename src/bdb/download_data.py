import shutil
from pathlib import Path

import kagglehub

COMPETITION = "nfl-big-data-bowl-2027"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

def main():
    cache_path = kagglehub.competition_download(COMPETITION)
    print(f"Downloaded data to {cache_path}")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copytree(cache_path, RAW_DIR, dirs_exist_ok=True)
    print(f"Copied data to {RAW_DIR}")

if __name__ == "__main__":
    main()