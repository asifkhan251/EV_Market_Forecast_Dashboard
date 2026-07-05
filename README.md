# 🔋 EV Market Strategic Growth & Grid Analytics Dashboard

An interactive, data-driven forecasting engine built using **Python, Scikit-Learn, and Streamlit**. This project models regional electric vehicle (EV) adoption trends and simulates the downstream energy demand constraints on electrical utility grids.

---

## 🤵 Developer Profile
* **Developer:** Asif khan 
* **Domain:** Electrical Engineering & Data Analytics
* **Project Status:** Production Ready / Completed
* **License:** MIT License

---

## 🚀 Key Features

* **Multi-Region Core Interface:** Interactive trends analysis covering **Global, India, China, and USA** automotive data segments.
* **Machine Learning Forecasting:** Implements a predictive **Linear Regression Model** via Scikit-Learn to compute real-time growth trajectories up to a 10-year horizon.
* **Electrical Grid Analytics:** Translates vehicle sales forecasts into actionable utility load curves, estimating daily incremental grid energy consumption in MegaWatt-hours ($MWh$).
* **Responsive Corporate UI:** Clean dashboard design supporting native responsive layouts for executive reviews, optimized with crisp visualizations and a permanent light mode theme.

---

## 📊 Methodology & Core Calculation

The simulation uses core automotive market metrics integrated with electrical power distribution equations to predict grid impact:

$$\text{Daily Incremental Energy Demand (MWh)} = \frac{\text{Projected EV Sales} \times \text{Avg. Daily Distance (km)} \times \text{Efficiency (kWh/km)}}{1000}$$

* **Default Engineering Assumptions:** Vehicle powertrain efficiency rating is locked at $0.16 \text{ kWh/km}$. Users can dynamically tweak daily driving distance and average battery capacity via sidebar sliders to observe real-time grid scaling.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Dashboard layout, sidebar parameters, and metric cards |
| **Data Handling** | Pandas & NumPy | CSV ingestion, sorting, filtering, and structural math |
| **Machine Learning**| Scikit-Learn | Linear Regression engine for auto-generating forecast vectors |
| **Visualizations** | Plotly Express & Graph Objects | Dynamic line graphs, multi-variable scatter lines, and bar charts |

---

## 📁 Project Directory Structure
---

```text
📁 EV_Market_Forecast/
│
├── 📁 .streamlit/
│   └── 📄 config.toml         # Custom configuration for layout light theme
│
├── 📄 app.py                  # Main Streamlit web application & ML dashboard logic
├── 📄 generate_data.py        # Python backend script to generate authentic market trends
├── 📊 ev_sales_data.csv       # Clean relational dataset used by the web app
├── 📄 .gitignore              # Restricts runtime caches and local files from git tracking
└── 📄 README.md               # Executive project documentation (This file)

##⚙️ Setup & Local Installation
Follow these quick steps to set up and run this dashboard locally on your workstation:

1. Initialize Project Directory
git clone [https://github.com/asifkhan251/EV_Market_Forecast_Dashboard/edit/main/EV_Market_Forecast.git](https://github.com/asifkhan251/EV_Market_Forecast_Dashboard/edit/main/EV_Market_Forecast.git)
cd ev-market-forecast-dashboard
2. Install Dependencies
Ensure you have Python environment configured, then run:
pip install streamlit pandas numpy plotly scikit-learn
3. Generate the Dataset
Execute the data engineering script to generate the authentic historical data:

Bash
```python generate_data.py```
4. Run the Streamlit Application
Bash
```streamlit run app.py```
The application will instantly launch in your default web browser at http://localhost:8501
##💡 Engineering Insights Provided
Grid Readiness Mapping: Pinpoints the exact target year when regional distribution utilities must upgrade localized substations and distribution transformers to handle peak residential charging loads.

Market Penetration S-Curves: Tracks the transition of EVs from niche tech enthusiast segments into massive mainstream transport fleets, helping plan public charging grid distribution.

Developed with ⚡ by Asif Khan as a cross-domain integration of Electrical Grid Infrastructure and Predictive Data Science.
