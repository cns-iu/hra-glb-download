import os
import requests
import argparse
import json
from urllib.parse import urlparse


def main():
    """A function to get download URLs for all 3D Reference Objects in the HRA, then download GLB files into a folder
    """

    # get data from HRA API endpoint
    endpoint = "https://apps.humanatlas.io/api/v1/reference-organs"

    # Use `argparse` to build URL
    parser = argparse.ArgumentParser(
        description="Download GLB files from CCF API")
    parser.add_argument("--url", type=str,
                        help="URL of the API", default=endpoint)
    parser.add_argument("--output-folder", type=str,
                        help="Folder to save downloaded GLB files", default="downloaded_organs/")
    parser.add_argument("--csv-file", type=str,
                        help="Path to the output CSV file", default="organ_files.csv")
    args, unknown = parser.parse_known_args()
    api_url = args.url

    # send request
    response = requests.get(api_url).text
    data = json.loads(response)
    print(data)

    # Make folder for GLB files or check if already present
    os.makedirs(args.output_folder, exist_ok=True)

    # Get download URLs
    for organ in data:
        glb_url = organ['object']['file']
        parsed_url = urlparse(glb_url)
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(args.output_folder, file_name)
        if glb_url:
            glb_response = requests.get(glb_url)
            if glb_response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(glb_response.content)
                    print(f"Downloaded {file_name}")


if __name__ == "__main__":
    main()
