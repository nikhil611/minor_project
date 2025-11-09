# utils.py
import matplotlib.pyplot as plt
import streamlit as st

def show_header():
    st.markdown(
        """
        <style>
        .big-title {font-size: 40px; font-weight: 700; color: #00C896;}
        .sub-title {font-size: 18px; color: #CCCCCC;}
        </style>
        <div class="big-title">💼 InvestSmartAI</div>
        <div class="sub-title">Your Rule-Based Investment Advisor</div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

def show_portfolio_chart(alloc):
    labels = list(alloc.keys())
    sizes = list(alloc.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

def card(title, content):
    st.markdown(
        f"""
        <div style="padding:20px;border-radius:15px;background-color:#1E222A;margin-bottom:10px;">
            <h4 style="color:#00C896;">{title}</h4>
            <p style="font-size:18px;">{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
