import streamlit as st
import plotly.graph_objects as go
from streamlit.components.v1 import html
import markdown


# ---------------- HEADER ----------------
def show_header():
    st.markdown("""
        <div class="main-header">
            <h1>💼 InvestSmartAI</h1>
            <p>Your AI-powered Financial Advisor — Smarter. Safer. Simpler.</p>
        </div>
    """, unsafe_allow_html=True)



# ---------------- PORTFOLIO CHART ----------------
def show_portfolio_chart(alloc: dict, theme="dark"):
    """
    Display an adaptive, modern donut-style portfolio chart with dynamic theming.

    Parameters
    ----------
    alloc : dict -> {"Stocks": 40, "Bonds": 25, "Gold": 20, "Crypto": 15}
    theme : str -> "dark" or "light"
    """
    if not alloc:
        st.warning("⚠️ No allocation data to display.")
        return

    labels = list(alloc.keys())
    values = list(alloc.values())

    if any(v < 0 for v in values):
        st.error("Portfolio allocation contains negative values.")
        return

    total = sum(values)
    if total == 0:
        st.warning("All values are zero — nothing to display.")
        return

    # Normalize
    values = [round((v / total) * 100, 2) for v in values]

    # THEME SETTINGS
    if theme == "dark":
        bg_color = "rgba(14,17,23,1)"
        text_color = "#FFFFFF"
        border_color = "#0E1117"
        palette = [
            "#00C896", "#EF553B", "#636EFA", "#AB63FA",
            "#FFA15A", "#19D3F3", "#FF6692", "#B6E880",
        ]
    else:
        bg_color = "#FFFFFF"
        text_color = "#000000"
        border_color = "#EAEAEA"
        palette = [
            "#007F5F", "#FF6B6B", "#4E79A7", "#A0CBE8",
            "#F28E2B", "#76B7B2", "#E15759", "#59A14F",
        ]

    # PIE CHART
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.35,
                pull=[0.05] * len(labels),
                textinfo="label+percent",
                textfont=dict(size=15, color=text_color),
                hoverinfo="label+value+percent",
                marker=dict(
                    colors=palette,
                    line=dict(color=border_color, width=2),
                ),
            )
        ]
    )

    fig.update_layout(
        title=dict(
            text="Portfolio Allocation",
            x=0.5,
            xanchor="center",
            font=dict(size=22, color=text_color, family="Arial Black"),
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            font=dict(size=13, color=text_color),
        ),
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        margin=dict(t=80, b=0, l=0, r=0),
        transition={"duration": 500, "easing": "cubic-in-out"},
    )

    st.plotly_chart(fig, use_container_width=True)

def md_to_html(text: str) -> str:
    """Convert markdown (like **bold**) to HTML tags."""
    return markdown.markdown(text)

# ---------------- CARD COMPONENT ----------------
def card(title: str, content: str, theme="dark"):
    """
    Displays a styled, balanced card with theme-aware colors and consistent spacing.
    """
    if theme == "dark":
        bg = "#1E222A"
        text = "#FFFFFF"
        accent = "#00C896"
        shadow = "0 0 20px rgba(0, 200, 150, 0.15)"
    else:
        bg = "#DBDBDB"
        text = "#000000"
        accent = "#007F5F"
        shadow = "0 0 15px rgba(0, 0, 0, 0.08)"

    html(
        f"""
        <div style="
            background-color:{bg};
            color:{text};
            border-radius: 18px;
            padding: 10px 20px;
            margin: 10px 0 15px 0;  /* tight, even spacing between cards */
            box-shadow: {shadow};
            transition: all 0.4s ease-in-out;
            height: 170px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <h4 style="margin-bottom:10px; color:{accent}; font-weight:700;">{title}</h4>
            <p style="font-size:16px; line-height:1.6; margin:0;">{md_to_html(content)}
</p>
        </div>
        """,
        height=210,  # minimal buffer for shadow, not excessive
    )
