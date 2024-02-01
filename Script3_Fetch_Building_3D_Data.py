import requests
import json

def fetch_3d_particles(building_ids):
    # URL of the API endpoint
    url = 'https://devkluster.ehr.ee/api/3dtwin/v1/rest-api/particles'

    # Headers to specify that we accept JSON
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Data payload with the building IDs
    payload = building_ids  # Directly use the list of building IDs

    # Making the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors or unsuccessful responses
        print(f"Error fetching data: {response.status_code}")
        return None

def save_data_to_file(building_id, data):
    filename = f"{building_id}.3D.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    building_ids = ["101015900", "101020224", "101020045","101020052","101043661"]
    print("Fetching 3D particles data for Building IDs:")
    for building_id in building_ids:
        print(f"Building ID: {building_id}")
        # Fetch data for each building ID separately
        data = fetch_3d_particles([building_id])  # Pass each ID as a list
        if data is not None:
            save_data_to_file(building_id, data)
