# URL to call: http://grlc.io/api-git/hubmapconsortium/ccf-grlc/subdir/ccf//ref-organ-glb-files?endpoint=https%3A%2F%2Fccf-api.hubmapconsortium.org%2Fv1%2Fsparql
import os
import requests
import csv
from urllib.parse import urlparse

def main():
    # First, we call the CCF API with a SPARQL query, all via grlc.io: http://grlc.io/api/hubmapconsortium/ccf-grlc/ccf/#/default/get_ref_organ_glb_files
    url = "http://grlc.io/api-git/hubmapconsortium/ccf-grlc/subdir/ccf//ref-organ-glb-files?endpoint=https%3A%2F%2Fccf-api.hubmapconsortium.org%2Fv1%2Fsparql?format=application/json"
    response = requests.get(url).json()
    
    # let's print the response to check that we received the expected response
    print(response)
    
    # Now, we need to loop through all the objects in the response and call the glb_url and download the GLB (3D) file that is returned
    # Then, we download each GLB file into the downloaded_organs folder
    save_path = "downloaded_organs/"
    os.makedirs(save_path, exist_ok=True)
    
    downloaded_url = []

    # Output a CSV with a mapping of reference organ, scene node, and download URL
    csvp = "organ_files.csv"
    with open(csvp,"w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ref_organ", "scene_node", "URL"])

    # Loop through API response and download all GLBs into a folder
        for i in response:
            glb_url = i['glb_url'].strip('"')
            organ_name = i['scene_node'].strip('"')
            new_n = urlparse(glb_url)
            file_name = os.path.splitext(os.path.basename(new_n.path))[0]
            glb_response = requests.get(glb_url)
            if glb_response.status_code == 200:
                file_path = os.path.join(save_path, f"{file_name}.glb") 
                with open(file_path, "wb") as file:
                    file.write(glb_response.content)
                    print(f"Downloaded {file_name}.glb")
                    downloaded_url.append(glb_url)
                    writer.writerow([i['ref_organ'].strip('"'),organ_name,glb_url])
    
if __name__ == "__main__":
    main()