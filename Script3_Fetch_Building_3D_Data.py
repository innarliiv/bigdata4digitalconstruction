import requests
import json

# Thanks to Anna-Liisa Hannus for the initial version of coordinate anonymization

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

def save_data_to_file(building_id, data, anonymize=True):
    # Set the filename based on whether anonymization is applied
    if anonymize:
        filename = f"{building_id}.anon.3D.json"
    else:
        filename = f"{building_id}.3D.json"
    
    if anonymize:
        # Anonymize and adjust data as needed
        for building in data:
            # Remove etak and ehr codes if present
            building.pop('etak', None)
            building.pop('ehr', None)

            # Initialize min values
            min_x, min_y, min_z = float('inf'), float('inf'), float('inf')

            # Find minimum x, y, z values for anonymization
            for particle in building.get("particles", []):
                for coord in ["x0", "x1", "x2"]:
                    if particle[coord] < min_x:
                        min_x = particle[coord]
                for coord in ["y0", "y1", "y2"]:
                    if particle[coord] < min_y:
                        min_y = particle[coord]
                for coord in ["z0", "z1", "z2"]:
                    if particle[coord] < min_z:
                        min_z = particle[coord]

            # Anonymize the data by adjusting x, y, z values
            for particle in building.get("particles", []):
                for coord in ["x0", "x1", "x2"]:
                    particle[coord] = particle[coord] - min_x
                for coord in ["y0", "y1", "y2"]:
                    particle[coord] = particle[coord] - min_y
                for coord in ["z0", "z1", "z2"]:
                    particle[coord] = particle[coord] - min_z

    # Save the modified or original data to a file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    building_ids = ["101015900", "101020224", "101020045", "101020052", "101043661"]
    print("Fetching 3D particles data for Building IDs:")
    for building_id in building_ids:
        print(f"Building ID: {building_id}")
        # Fetch data for each building ID separately
        data = fetch_3d_particles([building_id])  # Pass each ID as a list
        if data is not None:
            # Toggle anonymize to False if you do not want to anonymize the data
            save_data_to_file(building_id, data, anonymize=False)
