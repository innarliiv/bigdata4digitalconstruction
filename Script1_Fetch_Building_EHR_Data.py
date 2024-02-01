import requests
import json

def fetch_building_data(building_id):
    # URL of the API endpoint
    url = 'https://devkluster.ehr.ee/api/building/v2/buildingsData'

    # Headers to specify that we accept JSON and will send JSON
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Data payload with the building ID
    payload = {
        'ehrCodes': [building_id]  # This assumes the API expects a list, even for a single ID
    }

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
    filename = f"{building_id}.ehr.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    building_ids = ["101015900", "101020224"]
    for building_id in building_ids:
        print(f"Fetching data for Building ID: {building_id}")
        data = fetch_building_data(building_id)
        if data is not None:
            save_data_to_file(building_id, data)
