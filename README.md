# School of Information Technology, Tallinn University of Technology

Innar Liiv

# Building Data Visualization Toolkit

This repository contains a collection of Python scripts designed to fetch and visualize building data. These scripts are part of a toolkit that interacts with building data APIs to retrieve building information and 3D data, and then visualizes this information in both 2D and 3D formats. The toolkit is intended for use by developers, data analysts, urban planners, and architects who are interested in building data analysis and visualization.

## Scripts Overview

1. **Script1_Fetch_Building_EHR_Data.py**: Fetches building data from an API and saves it as JSON files.
2. **Script2_Draw_Building_TopDown_View.py**: Visualizes the top-down view of buildings using polygon data.
3. **Script3_Fetch_Building_3D_Data.py**: Retrieves 3D data of buildings for visualization purposes.
4. **Script4_Draw_Building_3D_View.py**: Generates a 3D visualization of buildings using fetched 3D data.

## Detailed Script Descriptions

### Script1_Fetch_Building_EHR_Data.py

This script fetches building data from the Building Registry (Ehitusregister - EHR) API. It sends a POST request to the API, processes the response, and saves the fetched data into JSON files for further analysis or visualization.

- **Key Features**: Efficient API interaction, error handling, and saving data for offline use.
- **Usage**: Modify the list of building IDs as required, then run the script to fetch and save the building data.

### Script2_Draw_Building_TopDown_View.py

Generates a 2D top-down view of a building from polygon data stored in a JSON file. This script is useful for spatial analysis and understanding the layout of a building or a set of buildings.

- **Key Features**: Polygon rotation for proper alignment, plotting with `matplotlib`, and customizable visualization options.
- **Usage**: Ensure the JSON file path is correctly specified, then run the script to visualize the building's top-down view.

### Script3_Fetch_Building_3D_Data.py

Communicates with a 3D Twin API to fetch detailed 3D particles data for specified building IDs. The script demonstrates batch processing capabilities and basic error management.

- **Key Features**: Batch processing of multiple building IDs, direct 3D data fetching, and saving the 3D data in a structured JSON format.
- **Usage**: Update the `building_ids` list with the IDs of interest, then execute the script to retrieve and save the 3D data.

### Script4_Draw_Building_3D_View.py

Visualizes 3D building data by rendering a detailed 3D model using `matplotlib`. This script provides an immersive way to examine a building's structure and design.

- **Key Features**: 3D rendering of building structures, color-coded visualization for clarity, and customizable view angles for detailed examination.
- **Usage**: Adjust the JSON file path to point to your 3D data file, then run the script to generate the 3D visualization.

## Installation and Requirements

To use these scripts, you will need Python installed on your system, along with the following libraries:

- `requests`
- `matplotlib`
- `numpy`

Install the required libraries using pip:

```sh
pip install requests matplotlib numpy
```

## Running the Scripts

### From Your Own Python Environment

1. Ensure Python and the required libraries are installed on your system.
2. Download the scripts from this repository to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the downloaded scripts.
5. Run a script using Python, for example:

```bash
python Script1_Fetch_Building_EHR_Data.py
```

### From Google Colab

1. Open a new notebook in Google Colab.
2. Upload the scripts to the Colab environment using the file upload feature.
3. Install the required libraries by running the following command in a cell:

```python
!pip install requests matplotlib numpy
```

4. Run the script by using the `!python` command in a cell, for example:

```python
!python Script1_Fetch_Building_EHR_Data.py
```

## Contributing

Contributions to this project are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or improvements you have made.
