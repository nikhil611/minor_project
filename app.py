# app.py
import streamlit as st
from rules import get_investment_allocation
from utils import show_header, show_portfolio_chart, card

# ---------------- CONFIG ----------------
st.set_page_config(page_title="InvestSmartAI", page_icon="💼", layout="centered")

# ---------------- THEME TOGGLE ----------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

toggle = st.sidebar.toggle("🌗 Toggle Theme", value=(st.session_state.theme == "dark"))
st.session_state.theme = "dark" if toggle else "light"

# Theme Colors
if st.session_state.theme == "dark":
    background_color = "#0E1117"
    secondary_bg = "#1E222A"
    text_color = "#00C896"
    accent = "#93993"
else:
    background_color = "#FFFFFF"
    secondary_bg = "#939393"
    text_color = "#111111"
    accent = "#007F5F"

# ---------------- GLOBAL CSS ----------------
st.markdown(f"""
    <style>
        html, body, [class*="css"] {{
            color: {text_color} !important;
            background-color: {background_color} !important;
            transition: all 0.6s ease-in-out;
        }}

        label, p, span, div, h1, h2, h3, h4, h5, h6 {{
            color: {text_color} !important;
            transition: color 0.6s ease-in-out;
        }}

        [data-testid="stAppViewContainer"],
        [data-testid="stSidebar"],
        [data-testid="stHeader"] {{
            background-color: {background_color} !important;
            color: {text_color} !important;
            transition: all 0.6s ease-in-out;
        }}

        [data-testid="stSidebar"] {{
            background-color: {secondary_bg} !important;
        }}

        .stButton>button {{
            background-color: {accent} !important;
            color: white !important;
            border: none;
            transition: background-color 0.3s ease-in-out;
            border-radius: 10px;
            font-weight: 600;
        }}

        .stButton>button:hover {{
            background-color: {accent}CC !important;
        }}

        .stAlert {{
            border-radius: 10px !important;
        }}

        .stTextInput > div > div > input,
        .stSelectbox > div > div > div {{
            color: {text_color} !important;
        }}

        /* === Header Styling === */
        .main-header {{
            text-align: center;
            margin-top: 20px;
            margin-bottom: 10px;
            position: relative;
        }}

        .main-header::after {{
            content: "";
            display: block;
            width: 700px;
            height: 2px;
            margin: 10px auto 0 auto;
            background-color: #808080;
            opacity: 0.4;
            border-radius: 2px;
        }}
    </style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
show_header()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25)
income = st.sidebar.number_input("Monthly Income (₹)", min_value=1000, value=50000)
risk = st.sidebar.selectbox("Risk Appetite", ["Low", "Moderate", "High"])
goal = st.sidebar.selectbox("Investment Goal", ["Short-term", "Long-term", "Retirement", "Wealth Creation"])

# ---------------- MAIN LOGIC ----------------
if st.sidebar.button("Get Investment Advice"):
    alloc, invest_amt = get_investment_allocation(age, income, risk, goal)

    st.success("✅ Based on your profile, here’s your recommended portfolio:")

    # Chart with theme-awareness
    show_portfolio_chart(alloc, theme=st.session_state.theme)

    # Cards
    card("📊 Portfolio Allocation", "<br>".join([f"{k}: {v}%" for k, v in alloc.items()]), theme=st.session_state.theme)
    card("💰 Suggested Monthly Investment", f"₹{invest_amt:,}", theme=st.session_state.theme)
    card("🧩 Advisor’s Note", f"For a **{risk.lower()}** risk profile at age {age}, this mix balances growth and stability toward your **'{goal}'** goal.", theme=st.session_state.theme)

else:
    st.info("👈 Fill out your details on the left and click **Get Investment Advice** to begin.")

st.markdown(
    """
    <hr>
    <p style='text-align:center; color:#6C757D; font-size:0.9rem;'>
        © 2025 InvestSmartAI | Built with ❤️
    </p>
    """,
    unsafe_allow_html=True,
)