# generate_data.py
import pandas as pd

# Real-world authentic trends ke mutabik dataset (with Global data)
data = [
    # --- GLOBAL TRENDS (Overall worldwide massive numbers) ---
    {"Year": 2018, "Region": "Global", "EV_Sales": 2100000, "Market_Share_Percentage": 2.5},
    {"Year": 2019, "Region": "Global", "EV_Sales": 2300000, "Market_Share_Percentage": 2.6},
    {"Year": 2020, "Region": "Global", "EV_Sales": 3100000, "Market_Share_Percentage": 4.2},
    {"Year": 2021, "Region": "Global", "EV_Sales": 6600000, "Market_Share_Percentage": 8.3},
    {"Year": 2022, "Region": "Global", "EV_Sales": 10500000, "Market_Share_Percentage": 13.0},
    {"Year": 2023, "Region": "Global", "EV_Sales": 13800000, "Market_Share_Percentage": 15.5},
    {"Year": 2024, "Region": "Global", "EV_Sales": 16500000, "Market_Share_Percentage": 17.0},
    {"Year": 2025, "Region": "Global", "EV_Sales": 20000000, "Market_Share_Percentage": 20.0},

    # --- INDIA (Slow start, massive boom after 2021) ---
    {"Year": 2018, "Region": "India", "EV_Sales": 1200, "Market_Share_Percentage": 0.04},
    {"Year": 2019, "Region": "India", "EV_Sales": 2000, "Market_Share_Percentage": 0.07},
    {"Year": 2020, "Region": "India", "EV_Sales": 5000, "Market_Share_Percentage": 0.15},
    {"Year": 2021, "Region": "India", "EV_Sales": 12000, "Market_Share_Percentage": 0.40},
    {"Year": 2022, "Region": "India", "EV_Sales": 48000, "Market_Share_Percentage": 1.50},
    {"Year": 2023, "Region": "India", "EV_Sales": 85000, "Market_Share_Percentage": 2.20},
    {"Year": 2024, "Region": "India", "EV_Sales": 120000, "Market_Share_Percentage": 3.10},
    {"Year": 2025, "Region": "India", "EV_Sales": 175000, "Market_Share_Percentage": 4.50},

    # --- CHINA (The Global Leader) ---
    {"Year": 2018, "Region": "China", "EV_Sales": 1100000, "Market_Share_Percentage": 4.0},
    {"Year": 2019, "Region": "China", "EV_Sales": 1200000, "Market_Share_Percentage": 4.8},
    {"Year": 2020, "Region": "China", "EV_Sales": 1340000, "Market_Share_Percentage": 5.4},
    {"Year": 2021, "Region": "China", "EV_Sales": 3500000, "Market_Share_Percentage": 15.0},
    {"Year": 2022, "Region": "China", "EV_Sales": 6500000, "Market_Share_Percentage": 25.0},
    {"Year": 2023, "Region": "China", "EV_Sales": 8100000, "Market_Share_Percentage": 31.0},
    {"Year": 2024, "Region": "China", "EV_Sales": 9500000, "Market_Share_Percentage": 36.0},
    {"Year": 2025, "Region": "China", "EV_Sales": 11000000, "Market_Share_Percentage": 42.0},

    # --- USA (Steady linear growth) ---
    {"Year": 2018, "Region": "USA", "EV_Sales": 360000, "Market_Share_Percentage": 2.1},
    {"Year": 2019, "Region": "USA", "EV_Sales": 330000, "Market_Share_Percentage": 1.9},
    {"Year": 2020, "Region": "USA", "EV_Sales": 290000, "Market_Share_Percentage": 2.0},
    {"Year": 2021, "Region": "USA", "EV_Sales": 600000, "Market_Share_Percentage": 4.2},
    {"Year": 2022, "Region": "USA", "EV_Sales": 1000000, "Market_Share_Percentage": 7.0},
    {"Year": 2023, "Region": "USA", "EV_Sales": 1400000, "Market_Share_Percentage": 9.1},
    {"Year": 2024, "Region": "USA", "EV_Sales": 1600000, "Market_Share_Percentage": 10.5},
    {"Year": 2025, "Region": "USA", "EV_Sales": 1900000, "Market_Share_Percentage": 12.0}
]

df = pd.DataFrame(data)
df.to_csv('ev_sales_data.csv', index=False)
print("New realistic dataset with Global data successfully created!")