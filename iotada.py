import requests
import json

# Adafruit IO credentials
username = '_slowpoke18'
key = 'feed key'
feed_key = 'feed name'

# Data to send
data = {
    'value': '20'
}

# Build the API URL
url = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key}/data"

# Add the Adafruit IO key to headers
headers = {
    'X-AIO-Key': key,
    'Content-Type': 'application/json'
}

# Send the data to Adafruit feed
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
