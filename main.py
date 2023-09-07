import time
from functions import get_supporters, get_donations, calculate_supporters_total_value

def main():
    supporters = get_supporters()
    donations = get_donations()

    if supporters and donations:
        supporter_total = {}

        for supporter in supporters:
            supporter_id = supporter["id"]
            supporter_name = supporter["name"]
            total_value = calculate_supporters_total_value(supporter_id, donations)
            supporter_total[supporter_name] = total_value

        for supporter_name, total_value in supporter_total.items():
            print(f"{supporter_name}: £{total_value}")
        else:
            print("The data requested is unavailable")



if __name__ == "__main__":
    main()