# app.py — Vaxikart Power BI Dashboard Showcase
import streamlit as st

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Vaxikart Dashboard Project",
    page_icon="💉",
    layout="wide"
)

st.title("💉 Vaxikart — Vaccine Ordering Insights Dashboard")

# ---------------------------------------------------
# Context
# ---------------------------------------------------
st.header("📌 Context")
st.markdown("""
Vaxikart is an application designed for healthcare professionals (HCPs) 
to order vaccines directly. While the platform enabled ordering across 
different vaccine brands, the marketing and outreach strategy had been 
randomized — offering the same communication to every HCP, with no 
personalization and no measurement of ROI.
""")

# ---------------------------------------------------
# Problem Statement
# ---------------------------------------------------
st.header("❓ Problem Statement")
st.markdown("""
The client faced challenges with:
- **Randomized strategy** for all HCPs with no customization.  
- Lack of **segmentation or targeting**.  
- No **ROI analysis** linking digital campaign engagement to purchase behavior.  

The goal was to design a **data-driven segmentation and campaign strategy** 
to improve uptake and engagement.
""")

# ---------------------------------------------------
# About the Data
# ---------------------------------------------------
st.header("📊 About the Data")
st.markdown("""
- **500 HCPs** across regions  
- **2 Vaccine brands** (A & B)  
- **3 years of order history** with purchase date, vaccine brand, and quantity  
- Campaign data including **reach, opens, clicks, and purchases**  
""")

# ---------------------------------------------------
# Actions
# ---------------------------------------------------
st.header("⚙️ Actions")
st.markdown("""
- Conducted **RFM (Recency, Frequency, Monetary) analysis** to segment HCPs.  
- Classified HCPs into:  
  - **Loyalists**  
  - **Fence-sitters**  
  - **Lost**  
- Applied **color coding** (Green = increasing, Amber = steady, Red = declining) 
  based on purchase trends in recent months.  
- Integrated **campaign engagement data** (reach → open → click → purchase) 
  with RFM segments.  
- Performed **ROI analysis** for each digital campaign to measure effectiveness 
  HCP-wise.  
""")

# ---------------------------------------------------
# Results
# ---------------------------------------------------
st.header("🏆 Results")
st.markdown("""
- Provided a **personalized strategy** per HCP with actionable insights for the sales team.  
- **Content strategy** aligned with RFM segments improved engagement by **25%**.  
- **Promotional campaigns** based on color coding boosted vaccine uptake by **45%**.  
- ROI tracking helped optimize future campaigns, ensuring targeted investment.  
""")

# ---------------------------------------------------
# Dashboard Screenshots
# ---------------------------------------------------
st.header("📸 Dashboard Screenshots")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Vaxikart Overview")
    st.image("Vaxikart_Overview.png", use_container_width=True)

with col2:
    st.subheader("HCP Segmentation")
    st.image("Vaxikart_HCP_Segmentation.png", use_container_width=True)

st.subheader("Campaign Analysis")
st.image("Vaxikart_Campaign_Analysis.png", use_container_width=True)
