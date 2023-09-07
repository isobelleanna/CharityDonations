import requests
import csv

base_url = "https://www.few-far.co/api/techtest/v1"

def get_supporters():
    response = requests.get(f"{base_url}/supporters")
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Status code: {response.status_code}- Could not retrieve supporters.")
        return []

def get_donations():
    response = requests.get(f"{base_url}/donations")
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Status code: {response.status_code}- Could not retrieve donations.")
        return []

def calculate_supporters_total_value(supporter_id, donations):
    total_value = 0
    for donation in donations:
        if donation["supporter_id"] == supporter_id:
            total_value += donation["amount"]
    return total_value


def export_lifetime_donation_to_csv(supporter_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["Supporter Name", "Total Donation (£)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for supporter_name, total_value in supporter_data.items():
            writer.writerow({'Supporter Name': supporter_name, 'Total Donation (£)': f"{total_value:.2f}"})


def post_export():
    response = requests.post(f"{base_url}/donations_exports")
    if response.status_code == 201:
        export_data = response.json()
        export_id = export_data["id"]
        print("Export successful.")
        return export_id
    else:
        print(f"Status code: {response.status_code}- Export failed.")
        return None


def check_export(export_id):
    response = requests.get(f"{base_url}/donations_exports/{export_id}")
    if response.status_code == 200:
        export_data = response.json()
        if export_data["status"] == "ready":
            print("Export ready.")
            print("Export URL:", export_data["url"])
            return True
        else:
            print("Export pending.")
            return False
    else:
        print(f"Status code: {response.status_code}- Checking export status failed.")
        return False


def combine_donations(export_url, donations):
    response = requests.get(export_url)
    if response.status_code == 200:
        export_data = response.json()
        export_donations = export_data.get("data", [])
        donations.extend(export_donations)
        print("Export data added to donations.")
    else:
        print(f"Status code: {response.status_code}- pulling export data failed.")

