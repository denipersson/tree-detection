import labelbox
import json

# Set up your Labelbox client with your API key
client = labelbox.Client(api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbHYybGlya3QwNDE4MDc1MzVrMm81bW5wIiwib3JnYW5pemF0aW9uSWQiOiJjbHYybGlya2UwNDE3MDc1M2Y0bzA4M3BoIiwiYXBpS2V5SWQiOiJjbHZjeWp4YnIwZGViMDczNDdsdXQ2b2F1Iiwic2VjcmV0IjoiZDRjYjBhM2ZlMWRjOTFhMjc5MDlhZTVmNmQxYWQzMmMiLCJpYXQiOjE3MTM5MTEzMjksImV4cCI6MjM0NTA2MzMyOX0.z-uigYwLe69Ms97eB4yOP0uPCA6Zncv6tE9TqQI7FxA')

# Define the parameters for exporting data
params = {
    "data_row_details": True,
    "metadata_fields": True,
    "attachments": True,
    "project_details": True,
    "performance_details": True,
    "label_details": True,
    "interpolated_frames": True
}

# Get your project using the project ID
project = client.get_project('clw7x348k0314072q32swa45r')
export_task = project.export_v2(params=params)

# Wait for the export to complete and check for errors
export_task.wait_till_done()
if export_task.errors:
    print(export_task.errors)
else:
    export_json = export_task.result

    # Save the JSON data to a file
    with open('exported_data.json', 'w') as f:
        json.dump(export_json, f)
