# 📱 M-Pesa Performance Dashboard (2021–2025)

An interactive Streamlit dashboard that visualises the performance of **M-Pesa** over time, focusing on revenue growth, customer usage patterns, transaction velocity, and the expansion of the merchant ecosystem.

This dashboard is designed to provide analysts, researchers, and business stakeholders with a clear, data-driven view of how M-Pesa is evolving from a simple transfer platform into a high-frequency financial lifestyle tool.

---

## 🔍 Overview

The dashboard presents insights across three main sections:

### 1. Executive Summary

* Key KPIs including:

  * Revenue
  * Active Users
  * Transaction Velocity
  * Total Transaction Value
* Revenue recovery trends post-COVID
* User growth and market saturation patterns

### 2. Usage & Velocity

* Comparison of:

  * Transaction Volume (Billions)
  * Transaction Value (Trillions KES)
* Monthly transaction velocity per user
* Highlights the shift towards micro-transactions and habitual usage

### 3. Merchant Ecosystem

* Growth of:

  * Pochi La Biashara (Informal merchants)
  * Lipa Na M-Pesa (Formal merchants)
* Visual comparison of merchant expansion trends
* Insight into dominance of informal sector digitisation

---

## 📊 Data Sources

All data used in this dashboard is derived from:

* Safaricom Annual Reports (FY2021 – FY2024)
* HY2025 Investor Briefing

⚠️ Note: FY2025 figures are projections based on half-year actuals and analyst annualisation assumptions.

---

## 🛠️ Technologies Used

* **Streamlit** – Web app framework
* **Pandas** – Data manipulation
* **Plotly & Plotly Express** – Interactive visualisations
* **Python 3.13** – Core language

---

## 🚀 Features

* Responsive wide-layout dashboard
* Styled metric cards with growth indicators
* Sidebar navigation for page switching
* Interactive charts with hover insights
* Cached data loading for performance
* Expandable data view for transparency

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/m-pesa-performance-dashboard.git
cd m-pesa-performance-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The dashboard is deployed on **Streamlit Cloud**. Ensure the following are included in your `requirements.txt`:

```
streamlit
pandas
plotly
```

---

## 📈 Key Insights Highlighted

* M-Pesa revenue shows consistent recovery and growth trajectory post-2021
* User growth is stabilising, but transaction intensity per user is rapidly increasing
* Pochi La Biashara is outperforming traditional merchant solutions in growth rate
* Rise of cashless micro-economies in Kenya’s informal sector

---

## 🌐 Live Demo

👉 **Live Dashboard:** [[https://your-streamlit-app-url.streamlit.app](https://lajema-m-pesa-performace-dashboard-app-0kcswg.streamlit.app/)

---

## 🖼️ Screenshots

> Add screenshots by placing images in a folder named `assets/` in your repository.

### Executive Summary View

![Executive Summary](assets/executive_summary.png)

### Usage & Velocity Analysis

![Usage & Velocity](assets/usage_velocity.png)

### Merchant Ecosystem View

![Merchant Ecosystem](assets/merchant_ecosystem.png)

---

## 🤖 AI Assistance & Credit

This dashboard structure, design logic, and analytical framing were developed with the assistance of **Google AI Studio**, which was used to support conceptualisation, layout ideation, and narrative refinement.

> Credit: Google AI Studio – AI-assisted development support

---

## 👤 Author

Created by a Data Analyst with a focus on financial inclusion, digital economies, and business intelligence storytelling.

---

## 📬 Feedback

Suggestions and improvements are welcome. Feel free to raise issues or submit pull requests to enhance functionality or visual depth.

---

### ✅ Status

Project is actively maintained and open for further analytical enhancements such as:

* County-level analysis
* Time-series forecasting
* Predictive merchant adoption modelling
* API-driven live data integration
