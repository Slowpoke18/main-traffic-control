import requests
import json

# Adafruit IO credentials
username = 'IO_USERNAME'
key = 'IO_KEY'
feed_key1 = 'lane1vehiclecount'
feed_key2 = 'lane2vehiclecount'
feed_key3 = 'lane3vehiclecount'
feed_key4 = 'lane4vehiclecount'
feed_key5 = 'lane1emeveh'
feed_key6 = 'lane2emeveh'
feed_key7 = 'lane3emeveh'
feed_key8 = 'lane4emeveh'

# Data to send
data1 = {
    'value': '1'
}

data2 = {
    'value': '2'
}

data3 = {
    'value': '3'
}

data4 = {
    'value': '4'
}

data5 = {
    'value': '5'
}

data6 = {
    'value': '6'
}

data7 = {
    'value': '7'
}

data8 = {
    'value': '8'
}
# Build the API URL
url1 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key1}/data"
url2 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key2}/data"
url3 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key3}/data"
url4 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key4}/data"
url5 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key5}/data"
url6 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key6}/data"
url7 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key7}/data"
url8 = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_key8}/data"

# Add the Adafruit IO key to headers
headers = {
    'X-AIO-Key': key,
    'Content-Type': 'application/json'
}

# Send the data to Adafruit feed
response1 = requests.post(url1, headers=headers, data=json.dumps(data1))
response2 = requests.post(url2, headers=headers, data=json.dumps(data2))
response3 = requests.post(url3, headers=headers, data=json.dumps(data3))
response4 = requests.post(url4, headers=headers, data=json.dumps(data4))
response5 = requests.post(url5, headers=headers, data=json.dumps(data5))
response6 = requests.post(url6, headers=headers, data=json.dumps(data6))
response7 = requests.post(url7, headers=headers, data=json.dumps(data7))
response8 = requests.post(url8, headers=headers, data=json.dumps(data8))

# Check the response status
if response1.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response1.status_code}")

if response2.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response2.status_code}")

if response2.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response2.status_code}")

if response3.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response4.status_code}")

if response4.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response4.status_code}")

if response5.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response5.status_code}")

if response6.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response6.status_code}")

if response7.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response7.status_code}")

if response8.status_code == 200:
    print("Data sent successfully to Adafruit feed.")
else:
    print(f"Failed to send data. Status code: {response8.status_code}")
