import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="EV Market Strategic Forecast", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    try:
        return pd.read_csv("ev_sales_data.csv")
    except FileNotFoundError:
        st.error("Missing Data: Please run 'generate_data.py' first.")
        st.stop()

df = load_data()

# --- SIDEBAR CONTROLS ---
st.sidebar.title("🕹️ Parameters & Controls")
selected_region = st.sidebar.selectbox("Region of Interest", df['Region'].unique())
forecast_period = st.sidebar.slider("Forecast Horizon (Years)", 1, 10, 5)

st.sidebar.header("🔌 Infrastructure Assumptions")
battery_cap = st.sidebar.slider("Avg. Battery Capacity (kWh)", 30, 100, 60)
daily_range = st.sidebar.slider("Avg. Daily Distance (km)", 10, 150, 40)
efficiency = 0.16  # Average kWh/km

# --- DATA PROCESSING & MODELING ---
region_df = df[df['Region'] == selected_region].sort_values('Year')

# ML Forecasting Logic (Linear Regression)
X = region_df[['Year']].values
y = region_df['EV_Sales'].values
model = LinearRegression().fit(X, y)

# Generating Predictions
last_yr = int(region_df['Year'].max())
future_yrs = np.arange(last_yr + 1, last_yr + 1 + forecast_period).reshape(-1, 1)
future_preds = np.clip(model.predict(future_yrs), 0, None).astype(int)

# Preparing Dataframes for Visualization
historic_data = pd.DataFrame({'Year': region_df['Year'], 'Sales': y, 'Status': 'Historical'})
forecast_data = pd.DataFrame({'Year': future_yrs.flatten(), 'Sales': future_preds, 'Status': 'Projected'})
combined_df = pd.concat([historic_data, forecast_data])

# --- DASHBOARD HEADER ---
st.title("🔋 EV Market Strategic Growth Dashboard")
st.markdown(f"**Analysis Focus:** Predictive Growth Modeling & Grid Impact Analysis for **{selected_region}**")

# --- TOP METRIC CARDS ---
m1, m2, m3, m4 = st.columns(4)
current_sales = int(y[-1])
projected_sales = int(future_preds[-1])
growth_pct = ((projected_sales - current_sales) / current_sales) * 100

m1.metric("Current Annual Sales", f"{current_sales:,}")
m2.metric("Projected Sales (Final Year)", f"{projected_sales:,}", f"{growth_pct:.1f}% Growth")
m3.metric("Market Share (Current)", f"{region_df['Market_Share_Percentage'].iloc[-1]}%")
m4.metric("Forecast Confidence", "High (Linear Trend)")

st.divider()

# --- MAIN VISUALIZATIONS ---
c1, c2 = st.columns(2)

with c1:
    st.subheader("📈 Market Adoption Curve")
    # Using explicit colorful palette lines
    fig_sales = px.line(combined_df, x='Year', y='Sales', color='Status',
                        markers=True,
                        color_discrete_map={"Historical": "#00CC96", "Projected": "#EF553B"},
                        labels={'Sales': 'Annual EV Sales Volume'})
    fig_sales.update_layout(hovermode="x unified", legend_title_text='')
    st.plotly_chart(fig_sales, use_container_width=True)

with c2:
    st.subheader("📊 Market Penetration Analysis")
    # Colorful gradient bar chart that stands out
    fig_share = px.bar(region_df, x='Year', y='Market_Share_Percentage',
                       color='Market_Share_Percentage', 
                       color_continuous_scale=px.colors.sequential.Viridis,
                       labels={'Market_Share_Percentage': 'Market Share (%)'})
    st.plotly_chart(fig_share, use_container_width=True)

st.divider()

# --- ELECTRICAL GRID ANALYSIS ---
st.subheader("⚡ Grid Infrastructure & Energy Demand Projection")
st.markdown("Quantifying the additional energy required from the utility grid based on the projected EV fleet size.")

# Energy Calculation: fleet_energy = Sales * (daily_km * efficiency) / 1000 for MWh
forecast_data['Energy_Demand_MWh'] = (forecast_data['Sales'] * daily_range * efficiency) / 1000

fig_energy = go.Figure()
fig_energy.add_trace(go.Scatter(x=forecast_data['Year'], y=forecast_data['Energy_Demand_MWh'],
                                mode='lines+markers', name='MWh Demand',
                                line=dict(color='#636EFA', width=4))) # Striking neon/blue color line
fig_energy.update_layout(xaxis_title="Year", yaxis_title="MWh per Day")
st.plotly_chart(fig_energy, use_container_width=True)

# --- PROFESSIONAL INSIGHT BOX ---
st.success(f"""
### 💡 Strategic Engineering Insights
* **Adoption Forecast:** By the year **{int(future_yrs[-1].item())}**, the market is expected to absorb **{projected_sales:,}** new electric vehicles annually.
* **Utility Impact:** The additional charging infrastructure for this projected fleet will require an estimated **{forecast_data['Energy_Demand_MWh'].max():.2f} MWh** of energy per day.
* **Grid Readiness:** Local utilities should prioritize substations and transformer upgrades in high-density urban areas to accommodate this load.
""")