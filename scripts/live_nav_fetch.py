import requests
import pandas as pd
import os

# Create folder for live NAV data
os.makedirs("data/raw/live_nav", exist_ok=True)

# Scheme Name : AMFI Code
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, amfi_code in schemes.items():

    try:
        url = f"https://api.mfapi.in/mf/{amfi_code}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Scheme details
        meta = data.get("meta", {})
        nav_data = data.get("data", [])

        print("\n" + "=" * 60)
        print(f"Requested Fund : {scheme_name}")
        print(f"AMFI Code      : {amfi_code}")
        print(f"API Scheme     : {meta.get('scheme_name', 'N/A')}")
        print(f"NAV Records    : {len(nav_data)}")

        if nav_data:
            df = pd.DataFrame(nav_data)

            file_path = f"data/raw/live_nav/{scheme_name}.csv"

            df.to_csv(file_path, index=False)

            print(f"Saved -> {file_path}")

    except Exception as e:
        print(f"Error fetching {scheme_name}: {e}")

print("\n" + "=" * 60)
print("LIVE NAV FETCH COMPLETED")
print("=" * 60)