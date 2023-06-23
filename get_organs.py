# URL to call: http://grlc.io/api-git/hubmapconsortium/ccf-grlc/subdir/ccf//ref-organ-glb-files?endpoint=https%3A%2F%2Fccf-api.hubmapconsortium.org%2Fv1%2Fsparql

import requests

def main():
    # First, we call the CCF API with a SPARQL query, all via grlc.io: http://grlc.io/api/hubmapconsortium/ccf-grlc/ccf/#/default/get_ref_organ_glb_files
    url = "http://grlc.io/api-git/hubmapconsortium/ccf-grlc/subdir/ccf//ref-organ-glb-files?endpoint=https%3A%2F%2Fccf-api.hubmapconsortium.org%2Fv1%2Fsparql?format=application/json"
    response = requests.get(url).json()
    
    # let's print the response to check that we received the expected response
    print(response)
    
    # Now, we need to loop through all the objects in the response and call the glb_url and download the GLB (3D) file that is returned
  
    # Then, we download each GLB file into the downloaded_organs folder
    save_path = "downloaded_organs/"
    
if __name__ == "__main__":
    main()