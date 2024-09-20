import requests
import time

# The URL to send the request to
url = "http://192.168.43.198/"

def check_object_detection():
    try:
        # Send a GET request to the server
        response = requests.get(url)
        
        # Check the response content, which is expected to be '0' or '1'
        if response.status_code == 200:
            if response.text.strip() == '1':
                print("Object detected")
            elif response.text.strip() == '0':
                print("No object detected")
            else:
                print("Unexpected response:", response.text)
        else:
            print("Failed to get a valid response. Status code:", response.status_code)
    
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)

if __name__ == "__main__":
    while True:
        # Check for object detection every 100ms
        check_object_detection()
        time.sleep(0.1)  # Sleep for 100ms (0.1 seconds)
