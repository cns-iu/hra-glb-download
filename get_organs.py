import os
import requests
import csv
import argparse
import json
from urllib.parse import urlparse

def main():
    link = "http://grlc.io/api-git/hubmapconsortium/ccf-grlc/subdir/ccf//ref-organ-glb-files?endpoint=https%3A%2F%2Fccf-api.hubmapconsortium.org%2Fv1%2Fsparql?format=application/json"
    parser = argparse.ArgumentParser(description="Download GLB files from CCF API")
    parser.add_argument("--url", type=str, help="URL of the API", default=link)
    parser.add_argument("--output-folder", type=str, help="Folder to save downloaded GLB files", default="downloaded_organs/")
    parser.add_argument("--csv-file", type=str, help="Path to the output CSV file", default="organ_files.csv")
    args, unknown = parser.parse_known_args()
    api_url = args.url

    response = requests.get(api_url).text

    data = json.loads(response)
    print(data)

    os.makedirs(args.output_folder, exist_ok=True)

    with open(args.csv_file, "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["ref_organ", "scene_node", "URL"])
        for item in data:
            glb_url = item.get('glb_url', '').strip('"')
            organ_name = item.get('scene_node', '').strip('"')
            parsed_url = urlparse(glb_url)
            file_name = os.path.basename(parsed_url.path)
            file_path = os.path.join(args.output_folder, file_name)
            if glb_url:
                glb_response = requests.get(glb_url)
                if glb_response.status_code == 200:
                    with open(file_path, "wb") as file:
                        file.write(glb_response.content)
                        print(f"Downloaded {file_name}")
                        writer.writerow([item.get('ref_organ', '').strip('"'), organ_name, glb_url])
                        
if __name__ == "__main__":
    main()