# app.py
# Final Streamlit app (images stored in the repo root / main branch)
# Expected files in the same folder as this app.py:
# - sentiment_chart_1.png
# - sentiment_chart_2.png

import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------
# Page configuration
# ----------------------------
st.set_page_config(
    page_title="Block, Inc. | AFT Project",
    page_icon="📊",
    layout="wide",
)

# ----------------------------
# Minimal styling
# ----------------------------
st.markdown(
    """
    <style>
      .main .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
      .card {
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 16px;
      }
      .placeholder {
        border: 2px dashed rgba(0,0,0,0.2);
        border-radius: 10px;
        padding: 60px;
        text-align: center;
        color: rgba(0,0,0,0.6);
        font-size: 0.95rem;
      }
      @media (prefers-color-scheme: dark) {
        .card { border: 1px solid rgba(255,255,255,0.15); }
        .placeholder { color: rgba(255,255,255,0.6); border-color: rgba(255,255,255,0.25); }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Paths (images in repo root)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent
IMG_SENT_1 = BASE_DIR / "sentiment_chart_1.png"
IMG_SENT_2 = BASE_DIR / "sentiment_chart_2.png"

# ----------------------------
# Static tables (fast)
# ----------------------------
products_df = pd.DataFrame(
    [
        ["Square", "Merchant payments, POS, SaaS tools", "Stable cash flows and high switching costs"],
        ["Cash App", "P2P, banking-lite, investing, Bitcoin", "High engagement and diversified monetization"],
        ["Afterpay", "BNPL services", "Links consumer demand with merchants"],
        ["TIDAL", "Creator monetization and streaming", "Supports creator economy strategy"],
        ["Spiral & TBD", "Bitcoin infrastructure and open-source tools", "Long-term decentralized finance vision"],
        ["Bitcoin Mining", "ASIC chips and mining hardware", "Vertical integration and cost efficiency"],
    ],
    columns=["Product", "What it does", "Strategic importance"],
)

btc_beta_df = pd.DataFrame(
    [
        ["Coinbase (COIN)", "0.6–0.8", "Highly sensitive to Bitcoin cycles"],
        ["Robinhood (HOOD)", "0.25–0.30", "Moderate crypto exposure"],
        ["Block (SQ)", "0.15–0.20", "Partial insulation via non-Bitcoin revenue"],
        ["PayPal (PYPL)", "~0.0", "Minimal crypto exposure"],
    ],
    columns=["Company", "Bitcoin Beta", "Interpretation"],
)

sentiment_df = pd.DataFrame(
    [
        ["Cash App", 72.65, "Strong UX, rewards, investing and Bitcoin features"],
        ["Google Pay", 69.25, "Reliable but limited financial features"],
        ["PayPal", 62.25, "Strong merchant use, weaker consumer sentiment"],
        ["Venmo", 60.90, "Social features but trust concerns"],
        ["Zelle", 54.75, "Fast transfers but low emotional attachment"],
    ],
    columns=["App", "Positive Sentiment (%)", "Key Insight"],
)

# ----------------------------
# Helpers
# ----------------------------
def show_image_or_placeholder(path: Path, placeholder_text: str, caption: str | None = None):
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.markdown(f'<div class="placeholder">{placeholder_text}<br><br><b>Missing:</b> {path.name}</div>', unsafe_allow_html=True)

# ----------------------------
# Sidebar navigation
# ----------------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Problem Statement",
        "Block & Products",
        "Competitive Analysis",
        "Sentiment Analysis",
        "Regulation & Bitcoin",
        "Key Takeaways",
    ],
)

# ----------------------------
# Header
# ----------------------------
st.title("Block, Inc. | Analytics for Finance Project")
st.caption("Fintech strategy, Bitcoin exposure, competitive risk, and sentiment analysis")
st.markdown("---")

# ----------------------------
# Sections
# ----------------------------
if section == "Overview":
    st.markdown(
        """
        <div class="card">
        <b>Project Overview</b><br><br>
        This Analytics for Finance project evaluates Block Inc.’s position at the intersection of
        traditional fintech and cryptocurrency markets. The analysis integrates asset pricing metrics,
        competitive benchmarking, consumer sentiment analysis, and regulatory assessment to understand
        Block’s risk-return profile and long-term strategy.
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Ticker", "SQ")
    c2.metric("Positioning", "Hybrid fintech + Bitcoin rails")
    c3.metric("Sentiment leader", "Cash App")

elif section == "Problem Statement":
    st.markdown(
        """
        <div class="card">
        <b>Problem Statement</b><br><br>
        • How exposed is Block Inc. to Bitcoin price movements?<br>
        • Does Block behave more like a fintech firm or a crypto-native company?<br>
        • How does Cash App sentiment compare with competing payment apps?<br>
        • Can regulation and consumer protection become a competitive advantage?
        </div>
        """,
        unsafe_allow_html=True,
    )

elif section == "Block & Products":
    st.subheader("Block and Its Products")
    st.dataframe(products_df, use_container_width=True, hide_index=True)

elif section == "Competitive Analysis":
    st.subheader("Bitcoin Exposure and Risk Positioning")
    st.dataframe(btc_beta_df, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)

    with col1:
        show_image_or_placeholder(
            IMG_SENT_1,
            "📈 Average Sentiment by App",
            caption="Average VADER sentiment by app",
        )

    with col2:
        show_image_or_placeholder(
            IMG_SENT_2,
            "📊 Sentiment Distribution (Positive / Neutral / Negative)",
            caption="Sentiment distribution across apps",
        )
    
elif section == "Sentiment Analysis":
    st.subheader("Cash App Sentiment Analysis (Google Play Reviews)")
    st.dataframe(sentiment_df, use_container_width=True, hide_index=True)

    st.markdown("### Chart Placeholder (optional)")
    st.markdown(
        '<div class="placeholder">📊 Add normalized price / volatility charts here if needed</div>',
        unsafe_allow_html=True,
    )
    
    st.markdown("### Sentiment Charts (images in repo root)")
    

elif section == "Regulation & Bitcoin":
    st.markdown(
        """
        <div class="card">
        <b>Regulation, Consumer Protection & Bitcoin Strategy</b><br><br>
        Block faced regulatory scrutiny related to AML and fraud controls, resulting in significant penalties.
        In response, the firm implemented scam reimbursements, improved fraud monitoring, and stricter identity
        verification. Block’s Bitcoin-first strategy focuses on regulated, trust-based access rather than broad
        multi-chain exposure.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif section == "Key Takeaways":
    st.markdown(
        """
        <div class="card">
        <b>Key Takeaways</b><br><br>
        • Block occupies a hybrid position between fintech stability and crypto volatility<br>
        • Bitcoin exposure is intentional but partially insulated by diversified revenue streams<br>
        • Cash App shows the strongest consumer sentiment among payment apps<br>
        • Regulation can shift from a risk to a competitive advantage through trust-building<br>
        • Bitcoin infrastructure and mining provide long-term strategic optionality
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption("Fast loading app • Images expected in repo root (same folder as app.py)")

