# app.py
# Streamlit app for the Block Inc AFT project README
# Run: streamlit run app.py

import os
from pathlib import Path

import pandas as pd
import streamlit as st


# ----------------------------
# Page config and light styling
# ----------------------------
st.set_page_config(
    page_title="Block, Inc. (SQ) | AFT Project",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
      .main .block-container { padding-top: 1.6rem; padding-bottom: 2rem; }
      h1, h2, h3 { letter-spacing: 0.2px; }
      .small-muted { color: rgba(250,250,250,0.65); font-size: 0.92rem; }
      .card {
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 14px 14px 8px 14px;
        background: rgba(255,255,255,0.02);
      }
      .kpi {
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 14px;
        background: rgba(255,255,255,0.02);
        height: 100%;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "readme_assets"
IMG_1 = ASSETS_DIR / "sentiment_chart_1.png"
IMG_2 = ASSETS_DIR / "sentiment_chart_2.png"

PDF_PATH = BASE_DIR / "Group 5_AFT Group Project.pdf"
PPT_PATH = BASE_DIR / "Group_5_Block Inc_ AFT.pptx"
NB_PATH = BASE_DIR / "AFT_Group_Project_Updated.ipynb"


# ----------------------------
# Data (tables from README)
# ----------------------------
products_df = pd.DataFrame(
    [
        {
            "Platform / Business": "Square (Seller ecosystem)",
            "What it does": "POS, payment processing, vertical SaaS (payroll, marketing, inventory), Square Banking",
            "Why it matters strategically": "Stable GPV-driven cash flows and merchant switching costs",
        },
        {
            "Platform / Business": "Cash App (Consumer super-app)",
            "What it does": "P2P, banking-lite, Cash Card and Boosts, investing, Bitcoin trading, tax filing",
            "Why it matters strategically": "Engagement and monetization across interchange, instant deposit fees, and spreads",
        },
        {
            "Platform / Business": "Afterpay (BNPL)",
            "What it does": "Pay-in-4 and merchant-integrated BNPL",
            "Why it matters strategically": "Links consumer demand to the merchant network and expands credit products",
        },
        {
            "Platform / Business": "TIDAL (Creator tools)",
            "What it does": "Music streaming and creator monetization tools",
            "Why it matters strategically": "Supports the broader economic empowerment narrative",
        },
        {
            "Platform / Business": "Spiral and TBD (Bitcoin infrastructure)",
            "What it does": "Open-source Bitcoin tools, Lightning development, decentralized identity and payments protocols",
            "Why it matters strategically": "Positions Block as a builder of long-term Bitcoin rails, not only a trading platform",
        },
        {
            "Platform / Business": "Bitcoin hardware and mining",
            "What it does": "ASIC chips, mining rigs, self-custody wallet initiatives",
            "Why it matters strategically": "Optionality via hardware revenue, pool fees, and lower execution costs for BTC trades",
        },
    ]
)

business_model_df = pd.DataFrame(
    [
        {
            "Company": "Block (SQ)",
            "Core model": "Seller payments, consumer finance, Bitcoin infrastructure",
            "Primary customer": "SMBs and underbanked or Gen Z consumers",
            "Role of crypto in strategy": "Central pillar (BTC trading, infrastructure, mining initiatives)",
        },
        {
            "Company": "PayPal (PYPL)",
            "Core model": "Global payments network",
            "Primary customer": "Merchants and mainstream consumers",
            "Role of crypto in strategy": "Minimal (buy and sell only)",
        },
        {
            "Company": "Coinbase (COIN)",
            "Core model": "Crypto exchange",
            "Primary customer": "Retail traders and institutions",
            "Role of crypto in strategy": "Core business (high cycle sensitivity)",
        },
        {
            "Company": "Robinhood (HOOD)",
            "Core model": "Retail brokerage",
            "Primary customer": "Young retail investors",
            "Role of crypto in strategy": "Material, mixed with equities and options cycles",
        },
    ]
)

btc_beta_df = pd.DataFrame(
    [
        {"Company": "COIN", "Estimated Bitcoin Beta (range)": "0.6 to 0.8", "Interpretation": "Strongly linked to BTC cycles"},
        {"Company": "HOOD", "Estimated Bitcoin Beta (range)": "0.25 to 0.30", "Interpretation": "Moderate exposure via retail crypto activity"},
        {"Company": "SQ", "Estimated Bitcoin Beta (range)": "0.15 to 0.20", "Interpretation": "Meaningful BTC linkage, partially insulated by non-BTC revenue"},
        {"Company": "PYPL", "Estimated Bitcoin Beta (range)": "0.0", "Interpretation": "Mostly independent of BTC cycles"},
    ]
)

volatility_df = pd.DataFrame(
    [
        {"Asset": "COIN", "Relative volatility level": "Highest", "What it implies": "Most sensitive to crypto market shocks"},
        {"Asset": "HOOD", "Relative volatility level": "High", "What it implies": "Retail trading cycle exposure"},
        {"Asset": "SQ", "Relative volatility level": "Moderate", "What it implies": "Hybrid fintech and crypto behavior"},
        {"Asset": "BTC", "Relative volatility level": "Moderate-high", "What it implies": "Crypto asset cyclicality"},
        {"Asset": "PYPL", "Relative volatility level": "Lowest", "What it implies": "Mature payments platform stability"},
    ]
)

sentiment_df = pd.DataFrame(
    [
        {"App": "Cash App", "Avg VADER (compound)": 0.37, "Positive %": 72.65, "Neutral %": 14.0, "Negative %": 13.0},
        {"App": "Google Pay", "Avg VADER (compound)": 0.27, "Positive %": 69.25, "Neutral %": 15.0, "Negative %": 15.0},
        {"App": "PayPal", "Avg VADER (compound)": 0.23, "Positive %": 62.25, "Neutral %": 17.0, "Negative %": 21.0},
        {"App": "Venmo", "Avg VADER (compound)": 0.22, "Positive %": 60.90, "Neutral %": 14.0, "Negative %": 25.0},
        {"App": "Zelle", "Avg VADER (compound)": 0.19, "Positive %": 54.75, "Neutral %": 21.0, "Negative %": 24.0},
    ]
)

penalties_df = pd.DataFrame(
    [
        {"Category": "Consumer refunds", "Amount (USD)": 120_000_000, "What it reflects": "Unresolved transaction alerts and consumer protection gaps"},
        {"Category": "State regulators (AML)", "Amount (USD)": 80_000_000, "What it reflects": "Weak AML controls and risk rating issues"},
        {"Category": "New York DFS", "Amount (USD)": 40_000_000, "What it reflects": "Broader crypto oversight failures"},
        {"Category": "Total", "Amount (USD)": 255_000_000, "What it reflects": "Compliance investment became unavoidable at scale"},
    ]
)

takeaways = [
    "Block sits between fintech and crypto-native peers with moderate BTC sensitivity and moderate volatility.",
    "Diversification across Square and Cash App partially insulates Block from pure crypto cycles.",
    "Cash App shows the strongest consumer sentiment, supporting a product-led advantage.",
    "Regulatory pressure is a strategic variable. Compliance and consumer protection can differentiate Block if rules tighten.",
    "Bitcoin mining and infrastructure are a long-term optionality play, not only a trading feature.",
]


# ----------------------------
# Helpers
# ----------------------------
def file_badge(path: Path, label: str):
    if path.exists():
        st.success(f"{label} found: {path.name}")
    else:
        st.warning(f"{label} not found: {path.name}")


def try_show_image(path: Path, caption: str):
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.info(f"Image not found: {path.as_posix()}")


# ----------------------------
# Sidebar nav
# ----------------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Problem Statement",
        "Block and Its Products",
        "Competitive Analysis",
        "Cash App Sentiment Analysis",
        "Regulation and Consumer Protection",
        "Bitcoin Strategy",
        "Key Takeaways",
        "Project Files",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Assets check**")
st.sidebar.caption("Place images in: readme_assets/")
file_badge(IMG_1, "sentiment_chart_1.png")
file_badge(IMG_2, "sentiment_chart_2.png")


# ----------------------------
# Header
# ----------------------------
st.title("Block, Inc. (SQ) | AFT Project Dashboard")
st.markdown(
    '<div class="small-muted">Competitive, risk, and sentiment analysis using market data, peer benchmarking, and Google Play review sentiment.</div>',
    unsafe_allow_html=True,
)
st.markdown("---")


# ----------------------------
# Sections
# ----------------------------
if section == "Overview":
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="kpi"><b>Company</b><br>Block, Inc. (NYSE: SQ)</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi"><b>Positioning</b><br>Hybrid fintech plus Bitcoin infrastructure</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi"><b>Methods</b><br>Returns, volatility, beta, sentiment, regulation</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
        <b>What this project does</b><br><br>
        Block operates across merchant payments (Square), consumer finance (Cash App), and Bitcoin-focused initiatives
        (Spiral, TBD, mining hardware). This dashboard summarizes the AFT analysis by combining:
        <ul>
          <li>Market behavior: normalized returns, volatility, and Bitcoin beta</li>
          <li>Business strategy: ecosystem products and competitive positioning</li>
          <li>Customer voice: sentiment analysis from Google Play reviews (2023 to 2025)</li>
          <li>Governance: regulation, consumer protection, and compliance response</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif section == "Problem Statement":
    st.subheader("Problem Statement")
    st.write(
        """
        1. Where does Block sit on the spectrum between traditional fintech and crypto-native firms?  
        2. How sensitive is Block to Bitcoin price movements (Bitcoin beta) and how does its volatility compare to peers?  
        3. Do Cash App user reviews indicate a competitive advantage in product experience and trust?  
        4. How do regulation and consumer protection shape Block’s strategic direction and risk profile?
        """
    )

elif section == "Block and Its Products":
    st.subheader("Block and Its Products")
    st.dataframe(products_df, use_container_width=True, hide_index=True)

elif section == "Competitive Analysis":
    st.subheader("Competitive Analysis")

    st.markdown("### Business model comparison")
    st.dataframe(business_model_df, use_container_width=True, hide_index=True)

    st.markdown("### Bitcoin beta summary")
    st.dataframe(btc_beta_df, use_container_width=True, hide_index=True)

    st.markdown("### Volatility positioning")
    st.dataframe(volatility_df, use_container_width=True, hide_index=True)

elif section == "Cash App Sentiment Analysis":
    st.subheader("Cash App Sentiment Analysis (Google Play Reviews, 2023 to 2025)")
    st.write(
        "Sentiment was scored using a VADER-based NLP pipeline on Google Play reviews to compare Cash App with peer apps."
    )

    st.markdown("### Summary table")
    st.dataframe(sentiment_df, use_container_width=True, hide_index=True)

    st.markdown("### Charts from the notebook output")
    colA, colB = st.columns(2)
    with colA:
        try_show_image(IMG_1, "Average VADER sentiment by app")
    with colB:
        try_show_image(IMG_2, "Sentiment distribution (Positive, Neutral, Negative)")

elif section == "Regulation and Consumer Protection":
    st.subheader("Regulation and Consumer Protection")
    st.write(
        """
        Block faced heightened regulatory scrutiny and responded with upgrades that emphasize trust and user protection,
        including scam reimbursement, AI-powered fraud tools, and stricter identity verification and AML oversight.
        """
    )

    st.markdown("### 2025 compliance and penalty overview")
    show_df = penalties_df.copy()
    show_df["Amount (USD)"] = show_df["Amount (USD)"].map(lambda x: f"${x:,.0f}")
    st.dataframe(show_df, use_container_width=True, hide_index=True)

    st.markdown("### Consumer protection response highlights")
    st.write(
        """
        - Scam reimbursement program  
        - AI-powered fraud detection and real-time monitoring  
        - Transaction warnings before suspicious transfers  
        - 24/7 support improvements  
        - Enhanced identity verification and Bitcoin due diligence
        """
    )

elif section == "Bitcoin Strategy":
    st.subheader("Bitcoin Strategy")
    st.write(
        """
        Block follows a Bitcoin-first approach and extends beyond trading into infrastructure and mining.
        This creates optionality through vertical integration, but also introduces compliance and market-structure risk.
        """
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Potential upside")
        st.write(
            """
            - Vertical integration across trading, custody, hardware, and mining  
            - Lower execution and settlement costs for Cash App BTC flows  
            - Differentiated positioning as a builder of Bitcoin rails
            """
        )
    with c2:
        st.markdown("#### Key risks")
        st.write(
            """
            - Regulatory uncertainty and state-by-state licensing complexity  
            - Higher compliance burden as scale increases  
            - Strategic risk if the market rewards multi-chain ecosystems over Bitcoin-only
            """
        )

elif section == "Key Takeaways":
    st.subheader("Key Takeaways")
    for t in takeaways:
        st.write(f"- {t}")

elif section == "Project Files":
    st.subheader("Project Files")
    st.write("If these files are in your repo root, you can access them here in the app.")

    col1, col2, col3 = st.columns(3)
    with col1:
        file_badge(PDF_PATH, "Report")
    with col2:
        file_badge(PPT_PATH, "Slides")
    with col3:
        file_badge(NB_PATH, "Notebook")

    st.markdown("### Downloads")
    st.caption("Streamlit supports downloading local files using a download button.")

    def add_download(path: Path, label: str):
        if not path.exists():
            st.info(f"{label} not found in app directory: {path.name}")
            return
        with open(path, "rb") as f:
            st.download_button(
                label=f"Download {label}",
                data=f,
                file_name=path.name,
                mime="application/octet-stream",
                use_container_width=True,
            )

    add_download(PDF_PATH, "Report (PDF)")
    add_download(PPT_PATH, "Slides (PPTX)")
    add_download(NB_PATH, "Notebook (IPYNB)")

st.markdown("---")
st.caption("Tip: Keep `readme_assets/sentiment_chart_1.png` and `readme_assets/sentiment_chart_2.png` in the repo so the charts render.")
