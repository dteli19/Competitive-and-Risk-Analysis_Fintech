# app.py
# Fast Streamlit app for Block Inc AFT project
# Run: streamlit run app.py

from pathlib import Path
import streamlit as st
import pandas as pd

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Block, Inc. (SQ) | AFT Project",
    page_icon="📊",
    layout="wide",
)

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "readme_assets"
IMG_1 = ASSETS_DIR / "sentiment_chart_1.png"
IMG_2 = ASSETS_DIR / "sentiment_chart_2.png"

PDF_PATH = BASE_DIR / "Group 5_AFT Group Project.pdf"
PPT_PATH = BASE_DIR / "Group_5_Block Inc_ AFT.pptx"
NB_PATH = BASE_DIR / "AFT_Group_Project_Updated.ipynb"

# ----------------------------
# Light CSS (kept minimal)
# ----------------------------
st.markdown(
    """
    <style>
      .main .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
      .card { border: 1px solid rgba(0,0,0,0.08); border-radius: 14px; padding: 14px; }
      .muted { color: rgba(0,0,0,0.6); }
      @media (prefers-color-scheme: dark){
        .card { border: 1px solid rgba(255,255,255,0.12); }
        .muted { color: rgba(255,255,255,0.65); }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Tables (static, fast)
# ----------------------------
products_df = pd.DataFrame(
    [
        ["Square (Seller ecosystem)", "POS + payments + SaaS + banking tools", "Stable GPV-driven cash flows and switching costs"],
        ["Cash App (Consumer super-app)", "P2P + banking-lite + Cash Card + investing + Bitcoin", "Engagement-led monetization across fees and spreads"],
        ["Afterpay (BNPL)", "Pay-in-4 BNPL", "Connects consumer demand with merchants; expands credit products"],
        ["TIDAL (Creator tools)", "Music streaming + creator monetization", "Supports economic empowerment narrative"],
        ["Spiral + TBD (Bitcoin infra)", "Open-source Bitcoin tools + identity/payment protocols", "Long-term Bitcoin rails strategy"],
        ["Bitcoin hardware and mining", "ASIC chips + mining rigs + self-custody", "Optionality: hardware revenue + lower BTC execution costs"],
    ],
    columns=["Platform / Business", "What it does", "Why it matters strategically"],
)

business_model_df = pd.DataFrame(
    [
        ["Block (SQ)", "Seller payments + consumer finance + Bitcoin infra", "SMBs + underbanked/Gen Z consumers", "Central pillar (BTC trading + infra + mining)"],
        ["PayPal (PYPL)", "Global payments network", "Merchants + mainstream consumers", "Minimal crypto (buy/sell only)"],
        ["Coinbase (COIN)", "Crypto exchange", "Retail traders + institutions", "Core business depends on crypto cycles"],
        ["Robinhood (HOOD)", "Retail brokerage", "Young retail investors", "Material crypto exposure, plus equity/options cycles"],
    ],
    columns=["Company", "Core model", "Primary customer", "Role of crypto in strategy"],
)

btc_beta_df = pd.DataFrame(
    [
        ["COIN", "0.6 to 0.8", "Strongly linked to BTC cycles"],
        ["HOOD", "0.25 to 0.30", "Moderate exposure via retail crypto activity"],
        ["SQ", "0.15 to 0.20", "Meaningful BTC linkage, partially insulated by non-BTC revenue"],
        ["PYPL", "0.0", "Mostly independent of BTC cycles"],
    ],
    columns=["Company", "Estimated Bitcoin Beta (range)", "Interpretation"],
)

volatility_df = pd.DataFrame(
    [
        ["COIN", "Highest", "Most sensitive to crypto market shocks"],
        ["HOOD", "High", "Retail trading cycle exposure"],
        ["SQ", "Moderate", "Hybrid fintech and crypto behavior"],
        ["BTC", "Moderate-high", "Crypto asset cyclicality"],
        ["PYPL", "Lowest", "Mature payments platform stability"],
    ],
    columns=["Asset", "Relative volatility level", "What it implies"],
)

sentiment_df = pd.DataFrame(
    [
        ["Cash App", 0.37, 72.65, 14.0, 13.0],
        ["Google Pay", 0.27, 69.25, 15.0, 15.0],
        ["PayPal", 0.23, 62.25, 17.0, 21.0],
        ["Venmo", 0.22, 60.90, 14.0, 25.0],
        ["Zelle", 0.19, 54.75, 21.0, 24.0],
    ],
    columns=["App", "Avg VADER (compound)", "Positive %", "Neutral %", "Negative %"],
)

penalties_df = pd.DataFrame(
    [
        ["Consumer refunds", 120_000_000, "Transaction alerts + consumer protection gaps"],
        ["State regulators (AML)", 80_000_000, "AML controls and risk rating issues"],
        ["New York DFS", 40_000_000, "Crypto oversight failures"],
        ["Total", 255_000_000, "Compliance investment at scale"],
    ],
    columns=["Category", "Amount (USD)", "What it reflects"],
)

takeaways = [
    "Block sits between fintech and crypto-native peers with moderate BTC sensitivity and moderate volatility.",
    "Diversification across Square and Cash App partially insulates Block from pure crypto cycles.",
    "Cash App shows the strongest consumer sentiment, supporting a product-led advantage.",
    "Regulatory pressure is a strategic variable; compliance can differentiate Block as rules tighten.",
    "Bitcoin mining and infrastructure provide long-term optionality, not just trading exposure.",
]

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Products",
        "Competitive Analysis",
        "Sentiment Analysis",
        "Regulation",
        "Key Takeaways",
        "Downloads",
    ],
)

# ----------------------------
# Header
# ----------------------------
st.title("Block, Inc. (SQ) | AFT Project")
st.markdown('<div class="muted">Fast summary app: tables + charts + downloads.</div>', unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Pages
# ----------------------------
if section == "Overview":
    st.markdown(
        """
        <div class="card">
        <b>Overview</b><br><br>
        This project analyzes Block, Inc. as a hybrid fintech platform (Square + Cash App) with intentional Bitcoin exposure.
        We combine competitive benchmarking (peers), Bitcoin beta and volatility insights, consumer sentiment for Cash App,
        and the impact of regulation and consumer protection.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Ticker", "SQ")
    col2.metric("Positioning", "Hybrid fintech + Bitcoin rails")
    col3.metric("Sentiment leader", "Cash App")

elif section == "Products":
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

elif section == "Sentiment Analysis":
    st.subheader("Cash App Sentiment Analysis (2023 to 2025)")
    st.dataframe(sentiment_df, use_container_width=True, hide_index=True)

    st.markdown("### Charts")
    c1, c2 = st.columns(2)

    with c1:
        if IMG_1.exists():
            st.image(str(IMG_1), use_container_width=True)
        else:
            st.info("Missing image: readme_assets/sentiment_chart_1.png")

    with c2:
        if IMG_2.exists():
            st.image(str(IMG_2), use_container_width=True)
        else:
            st.info("Missing image: readme_assets/sentiment_chart_2.png")

elif section == "Regulation":
    st.subheader("Regulation and Consumer Protection")
    show_df = penalties_df.copy()
    show_df["Amount (USD)"] = show_df["Amount (USD)"].map(lambda x: f"${x:,.0f}")
    st.dataframe(show_df, use_container_width=True, hide_index=True)

    st.markdown("### What changed")
    st.write(
        "- Scam reimbursement and stronger fraud tooling\n"
        "- Real-time monitoring and transaction warnings\n"
        "- Enhanced identity verification and Bitcoin due diligence\n"
        "- Independent oversight and tighter AML processes"
    )

elif section == "Key Takeaways":
    st.subheader("Key Takeaways")
    for t in takeaways:
        st.write(f"- {t}")

elif section == "Downloads":
    st.subheader("Project Files")
    st.caption("Downloads only work if these files are in your repo root.")

    def download_file(path: Path, label: str):
        if not path.exists():
            st.info(f"{label} not found: {path.name}")
            return
        with open(path, "rb") as f:
            st.download_button(
                label=f"Download {label}",
                data=f,
                file_name=path.name,
                mime="application/octet-stream",
                use_container_width=True,
            )

    download_file(PDF_PATH, "Report (PDF)")
    download_file(PPT_PATH, "Slides (PPTX)")
    download_file(NB_PATH, "Notebook (IPYNB)")

st.markdown("---")
st.caption("Keep images in `readme_assets/` so they render quickly.")
