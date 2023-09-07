import time
from functions import get_supporters, get_donations, calculate_supporters_total_value, export_lifetime_donation_to_csv, post_export, check_export, combine_donations

base_url = "https://www.few-far.co/api/techtest/v1"


def main():
    supporters = get_supporters()
    donations = get_donations()

    export_id = post_export()
    if export_id:
        while not check_export(export_id):
            time.sleep(20)
        export_url = f"{base_url}/donations_exports/{export_id}"
        combine_donations(export_url, donations)

    if supporters and donations:
        supporter_total = {}

        for supporter in supporters:
            supporter_id = supporter["id"]
            supporter_name = supporter["name"]
            total_value = calculate_supporters_total_value(supporter_id, donations)
            supporter_total[supporter_name] = total_value

        export_lifetime_donation_to_csv(supporter_total, "lifetime_donation.csv")
        print("CSV file is ready.")

    else:
        print("The data requested is unavailable.")


if __name__ == "__main__":
    main()