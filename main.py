import json

def get_company_data_feeds_for_day(day):
    with open(f"data/company_feeds/day_{day}/company_a.json") as f:
        properties_company_a = json.load(f)
    with open(f"data/company_feeds/day_{day}/company_b.json") as f:
        properties_company_b = json.load(f)
    with open(f"data/company_feeds/day_{day}/company_c.json") as f:
        properties_company_c = json.load(f)
    return properties_company_a, properties_company_b, properties_company_c

def update_properties_status(properties, previous_snapshot):
    updated_properties = {}

    # If there is a previous snapshot, load it
    if previous_snapshot:
        with open(previous_snapshot, 'r') as snapshot_file:
            updated_properties = json.load(snapshot_file)
    
    # Create a set of addresses for the current day's properties
    current_addresses = {property_info['address'] for property_info in properties}

    # Mark properties in the current feed as actively listed
    for address in current_addresses:
        updated_properties[address] = "actively_listed"

    # Mark properties not included in the current feed as off-market
    for address in updated_properties.keys():
        if address not in current_addresses:
            updated_properties[address] = "off_market"

    return updated_properties



def generate_snapshot_for_day(day, properties_company_a, properties_company_b, properties_company_c):
    properties_for_day = properties_company_a + properties_company_b + properties_company_c

    # Get the previous snapshot for updating property status
    previous_snapshot = f"data/snapshots/day_{day-1}.json" if day > 0 else None

    # Update property status
    updated_properties = update_properties_status(properties_for_day, previous_snapshot)

    # Save updated snapshot to a JSON file
    with open(f"data/snapshots/day_{day}.json", 'w') as f:
        json.dump(updated_properties, f, indent=4)

if __name__ == "__main__":
    CURRENT_DAY = 0 

    while CURRENT_DAY < 3:  # Adjust this loop to generate snapshots for desired number of days
        properties_company_a, properties_company_b, properties_company_c = get_company_data_feeds_for_day(CURRENT_DAY)
        generate_snapshot_for_day(CURRENT_DAY, properties_company_a, properties_company_b, properties_company_c)
        CURRENT_DAY += 1
