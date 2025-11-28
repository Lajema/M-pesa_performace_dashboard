import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------------------------------------------------
# 1. Page Configuration & Styling
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="M-Pesa Performance Dashboard (2021-2025)",
    page_icon="📱",
    layout="wide"
)

# Custom CSS to style the metrics and headers
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #0e1117;
    }
    .metric-label {
        font-size: 14px;
        color: #555;
    }
    .metric-delta {
        font-size: 12px;
        color: #28a745; 
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Data Loading (Hardcoded from Safaricom Annual Reports)
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    # Main Financials & Usage Data
    data = {
        'Fiscal_Year': ['2021', '2022', '2023', '2024', '2025 (Proj)'],
        'Revenue_Bn': [82.65, 107.69, 117.19, 139.91, 161.12],
        'Active_Users_M': [28.31, 30.53, 32.11, 32.41, 35.82],
        'Txn_Velocity_Monthly': [16.2, 20.3, 23.5, 31.5, 37.9],  # Transactions per user
        'Total_Txn_Value_Trn': [22.04, 29.55, 35.86, 40.24, 43.50],
        'Total_Txn_Volume_Bn': [11.68, 15.75, 21.03, 28.33, 37.20]
    }
    
    # Merchant (Lipa Na M-Pesa) specific data
    merchant_data = {
        'Fiscal_Year': ['2023', '2024', '2025 (HY)'],
        'Pochi_Active_Tills': [292634, 632681, 869000],
        'LNM_Active_Merchants': [606660, 633000, 658700]
    }
    
    return pd.DataFrame(data), pd.DataFrame(merchant_data)

df, df_merchant = load_data()

# -----------------------------------------------------------------------------
# 3. Sidebar Navigation
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", ["Executive Summary", "Usage & Velocity", "Merchant Ecosystem"])
    
    st.markdown("---")
    st.markdown("**Data Source:**\nSafaricom Annual Reports (FY21-FY24) & HY25 Investor Briefing.")
    st.info("💡 **Analyst Note:** FY25 figures are based on HY25 actuals annualized + analyst projections.")

# -----------------------------------------------------------------------------
# 4. Helper Function for Metric Cards
# -----------------------------------------------------------------------------
def display_metric(label, value, delta):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-delta"> {delta}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PAGE 1: Executive Summary
# -----------------------------------------------------------------------------
if page == "Executive Summary":
    st.title("📊 Executive Summary: M-Pesa Performance")
    st.markdown("Tracking the post-Covid recovery and the shift towards high-frequency usage.")

    # Top Row Metrics (Using latest FY25 Proj vs FY24)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric("Revenue (FY25 Proj)", "KES 161.1B", "↑ 15.2% YoY")
    with col2:
        display_metric("Active Cust. (1-Mo)", "35.82 M", "↑ 10.5% YoY")
    with col3:
        display_metric("Txn Velocity (Per User)", "37.9 / mo", "↑ 20.3% YoY")
    with col4:
        display_metric("Total Txn Value", "KES 43.5 Trn", "↑ 8.1% YoY")

    st.markdown("---")

    # Row 2: Revenue & User Growth
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("The Revenue Recovery Curve")
        fig_rev = px.line(df, x='Fiscal_Year', y='Revenue_Bn', markers=True, 
                          title='Annual Revenue Growth (KES Billions)',
                          color_discrete_sequence=['#28a745'])
        fig_rev.add_bar(x=df['Fiscal_Year'], y=df['Revenue_Bn'], name='Revenue', opacity=0.3)
        fig_rev.update_layout(showlegend=False, xaxis_title="Fiscal Year", yaxis_title="Revenue (Bn)")
        st.plotly_chart(fig_rev, use_container_width=True)

    with c2:
        st.subheader("Market Saturation?")
        fig_user = px.bar(df, x='Fiscal_Year', y='Active_Users_M', 
                          title='Active 1-Month Customers',
                          text_auto=True, color_discrete_sequence=['#006400'])
        fig_user.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig_user.update_layout(xaxis_title=None, yaxis_title="Users (Millions)")
        st.plotly_chart(fig_user, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 2: Usage & Velocity
# -----------------------------------------------------------------------------
elif page == "Usage & Velocity":
    st.title("📈 Usage Patterns: The Velocity Shift")
    st.markdown("""
    **Key Insight:** While user growth is stabilizing, **usage intensity** is exploding. 
    Customers are not just sending money; they are living their financial lives on the app.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        # Dual Axis Chart: Volume vs Value
        st.subheader("Transaction Volume vs. Value")
        
        fig = go.Figure()
        
        # Bar for Volume
        fig.add_trace(go.Bar(
            x=df['Fiscal_Year'],
            y=df['Total_Txn_Volume_Bn'],
            name='Volume (Bn)',
            marker_color='#b2d8b2',
            yaxis='y'
        ))
        
        # Line for Value
        fig.add_trace(go.Scatter(
            x=df['Fiscal_Year'],
            y=df['Total_Txn_Value_Trn'],
            name='Value (Trn KES)',
            mode='lines+markers',
            line=dict(color='darkgreen', width=3),
            yaxis='y2'
        ))
        
        fig.update_layout(
            yaxis=dict(title="Volume (Bn Transactions)", side="left"),
            yaxis2=dict(title="Value (Trn KES)", side="right", overlaying="y", showgrid=False),
            legend=dict(x=0.01, y=0.99),
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Velocity Area Chart
        st.subheader("Average Transactions Per User (Monthly)")
        
        fig_vel = px.area(df, x='Fiscal_Year', y='Txn_Velocity_Monthly',
                          markers=True, color_discrete_sequence=['#28a745'])
        
        fig_vel.add_annotation(
            x='2025 (Proj)', y=37.9,
            text="37.9 Txns/Mo",
            showarrow=True, arrowhead=1, ax=-40, ay=-40
        )
        fig_vel.update_layout(yaxis_title="Txns per User / Month")
        st.plotly_chart(fig_vel, use_container_width=True)

    st.info("""
    **Analyst Take:** The gap between Volume (Bars) and Value (Line) in the chart on the left is widening. 
    This confirms the rise of **micro-transactions** (paying for small goods, bodaboda, snacks) rather than just bulk rent/school fee transfers.
    """)

# -----------------------------------------------------------------------------
# PAGE 3: Merchant Ecosystem
# -----------------------------------------------------------------------------
elif page == "Merchant Ecosystem":
    st.title("🏪 The Merchant Ecosystem (Lipa Na M-Pesa)")
    st.markdown("The battle for the informal sector: **Pochi La Biashara** is the fastest growing segment.")

    # Calculate growth rates for the KPI cards
    pochi_growth = ((869000 - 632681) / 632681) * 100
    
    m1, m2 = st.columns(2)
    with m1:
        display_metric("Pochi Active Tills (HY25)", "869,000", f"↑ {pochi_growth:.1f}% vs FY24")
    with m2:
        display_metric("LNM Active Merchants (HY25)", "658,700", "↑ 4.1% vs FY24")

    st.markdown("---")
    
    # Visualizing the Pochi Explosion
    st.subheader("Formal vs. Informal Merchant Growth")
    
    # Reshaping data for grouped bar chart
    df_long = pd.melt(df_merchant, id_vars=['Fiscal_Year'], 
                      value_vars=['Pochi_Active_Tills', 'LNM_Active_Merchants'],
                      var_name='Merchant_Type', value_name='Count')
    
    # Renaming for clarity
    df_long['Merchant_Type'] = df_long['Merchant_Type'].replace({
        'Pochi_Active_Tills': 'Pochi (Informal)',
        'LNM_Active_Merchants': 'Lipa Na M-Pesa (Formal)'
    })
    
    fig_merch = px.bar(df_long, x='Fiscal_Year', y='Count', color='Merchant_Type',
                       barmode='group',
                       title="Active Merchants: Pochi vs. Standard Tills",
                       color_discrete_map={'Pochi (Informal)': '#ffbf00', 'Lipa Na M-Pesa (Formal)': '#28a745'},
                       text_auto='.2s')
    
    fig_merch.update_layout(yaxis_title="Active Tills")
    st.plotly_chart(fig_merch, use_container_width=True)

    with st.expander("View Underlying Data"):
        st.dataframe(df_merchant)