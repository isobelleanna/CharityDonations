import requests

base_url = "https://www.few-far.co/api/techtest/v1"

def get_supporters():
    supporters_url = f"{base_url}/supporters"
    response = requests.get(supporters_url)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Status code: {response.status_code}- Could not retrieve supporters")
        return []

def get_donations():
    donations_url = f"{base_url}/donations"
    response = requests.get(donations_url)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Status code: {response.status_code}- Could not retrieve donations")
        return []

def calculate_supporters_total_value(supporter_id, donations):
    total_value = 0
    for donation in donations:
        if donation["supporter_id"] == supporter_id:
            total_value += donation["amount"]
    return total_value