import requests
import time

SERVER_URL = 'http://129.97.168.82:5000'
CLIENT_ID = 'client1'

def attach():
    response = requests.post(f'{SERVER_URL}/attach', json={'client_id': CLIENT_ID})
    print(response.json())

def send_traffic():
    response = requests.post(f'{SERVER_URL}/send_traffic', json={'client_id': CLIENT_ID})
    print(response.json())

def detach():
    response = requests.post(f'{SERVER_URL}/detach', json={'client_id': CLIENT_ID})
    print(response.json())

if __name__ == '__main__':
    attach()
    time.sleep(2)  # Wait for 2 seconds before sending traffic
    send_traffic()
    time.sleep(4)  # Simulate traffic for 10 seconds
    detach()