import os
import gdown

def download_data():
    file_id = '1W7hnXOPg-QjxsjvDVwdX1QnKMOTnV4ci'

    # Get absolute project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, 'data')
    output = os.path.join(output_dir, 'crime_in_la.csv')

    os.makedirs(output_dir, exist_ok=True)

    gdown.download(id=file_id, output=output, quiet=False)

    if os.path.exists(output):
        print(f"Download successful")
    else:
        print("Download failed. File not found.")

if __name__ == "__main__":
    download_data()


