import json

def get_company_data_feeds_for_day(day):
    f = open(f"ps_challenge_one/data/company_feeds/day_{day}/company_a.json")
    properties_company_a = json.load(f)
    f = open(f"ps_challenge_one/data/company_feeds/day_{day}/company_b.json")
    properties_company_b = json.load(f)
    f = open(f"ps_challenge_one/data/company_feeds/day_{day}/company_c.json")
    properties_company_c = json.load(f)
    return properties_company_a, properties_company_b, properties_company_c

def generate_snapshot_for_day(day, properties_company_a, properties_company_b, properties_company_c):
    properties_for_day = properties_company_a + properties_company_b + properties_company_c
    properties_json = json.dumps(properties_for_day, indent = 4)
    with open(f"ps_challenge_one/data/snapshots/day_{day}.json", 'w') as f:
        f.write(properties_json)

if __name__ == "__main__":

    CURRENT_DAY = 0

    # ----------***** DAY 0 *****----------

    properties_company_a, properties_company_b, properties_company_c = get_company_data_feeds_for_day(CURRENT_DAY)
    # properties_company_a = api.post(properties_company_a)
    # properties_company_b = api.post(properties_company_b)
    # properties_company_c = api.post(properties_company_c)
    # ...
    generate_snapshot_for_day(CURRENT_DAY, properties_company_a, properties_company_b, properties_company_c)
    CURRENT_DAY += 1


    # ----------***** DAY 1 *****----------

    properties_company_a, properties_company_b, properties_company_c = get_company_data_feeds_for_day(CURRENT_DAY)
    # properties_company_a = api.post(properties_company_a)
    # properties_company_b = api.post(properties_company_b)
    # properties_company_c = api.post(properties_company_c)
    # ...
    generate_snapshot_for_day(CURRENT_DAY, properties_company_a, properties_company_b, properties_company_c)
    CURRENT_DAY += 1


    # ----------***** DAY 2 *****----------

    properties_company_a, properties_company_b, properties_company_c = get_company_data_feeds_for_day(CURRENT_DAY)
    # properties_company_a = api.post(properties_company_a)
    # properties_company_b = api.post(properties_company_b)
    # properties_company_c = api.post(properties_company_c)
    # ...
    generate_snapshot_for_day(CURRENT_DAY, properties_company_a, properties_company_b, properties_company_c)
    CURRENT_DAY += 1
