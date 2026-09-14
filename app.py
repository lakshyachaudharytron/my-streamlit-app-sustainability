import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sustainability | Sustainable Investment Insights",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# GLOBAL STYLING — Royal Blue & Gold identity
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'EB Garamond', serif;
    font-size: 1.05rem;
}

:root {
    --navy-deep: #12211C;
    --royal-blue: #1F4B3F;
    --royal-blue-light: #2F6A57;
    --gold: #AD8A55;
    --gold-light: #D9BE8F;
    --ivory: #F6F3EA;
    --text-dark: #201C14;
    --text-muted: #6B665A;
}

.stApp {
    background: linear-gradient(180deg, var(--navy-deep) 0%, var(--royal-blue) 100%);
}

section[data-testid="stSidebar"] {
    background-color: var(--navy-deep);
    border-right: 1px solid var(--gold);
}
section[data-testid="stSidebar"] * {
    color: #EAF0FB !important;
}
section[data-testid="stSidebar"] .stButton > button {
    background-color: transparent;
    color: #EAF0FB !important;
    border: 1px solid rgba(201, 162, 75, 0.35);
    text-align: left;
    justify-content: flex-start;
    font-weight: 600;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background-color: rgba(201, 162, 75, 0.18);
    border-color: var(--gold);
    color: var(--gold-light) !important;
}
section[data-testid="stSidebar"] div[data-testid="stExpander"] {
    border: 1px solid rgba(201, 162, 75, 0.35) !important;
    border-radius: 4px;
    margin-bottom: 0.4rem;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif;
    color: var(--gold-light);
    font-weight: 700;
    letter-spacing: 0.4px;
}

div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3 {
    color: var(--navy-deep);
}

p, .stMarkdown, label, .stCaption {
    color: #EAF0FB;
}
div[data-testid="stVerticalBlockBorderWrapper"] p,
div[data-testid="stVerticalBlockBorderWrapper"] .stMarkdown,
div[data-testid="stVerticalBlockBorderWrapper"] .stCaption {
    color: var(--text-dark);
}

hr {
    border-top: 1px solid var(--gold-light) !important;
}

div[data-testid="stAppViewContainer"] .stButton > button {
    background-color: var(--gold);
    color: var(--navy-deep);
    border: 1px solid var(--gold-light);
    border-radius: 4px;
    padding: 0.55rem 1.4rem;
    font-family: 'Lora', serif;
    font-weight: 700;
    letter-spacing: 0.4px;
    transition: all 0.25s ease;
}
div[data-testid="stAppViewContainer"] .stButton > button:hover {
    background-color: var(--gold-light);
    color: var(--navy-deep);
    border-color: var(--navy-deep);
}

.stTextInput > div > div > input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox > div > div {
    border-radius: 4px !important;
    border: 1px solid #D8CFB8 !important;
    background-color: white !important;
    color: var(--text-dark) !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 6px !important;
    border: 1px solid var(--gold) !important;
    background-color: var(--ivory) !important;
}

.badge {
    display: inline-block;
    background-color: var(--navy-deep);
    color: var(--gold-light);
    padding: 4px 14px;
    border-radius: 2px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.hero {
    padding: 3.5rem 3rem;
    border-radius: 6px;
    background: linear-gradient(135deg, var(--navy-deep) 0%, var(--royal-blue-light) 100%);
    border: 1px solid var(--gold);
    color: var(--ivory);
    margin-bottom: 2.2rem;
    position: relative;
}
.hero::before {
    content: "";
    position: absolute;
    top: 12px; left: 12px; right: 12px; bottom: 12px;
    border: 1px solid rgba(201, 162, 75, 0.4);
    border-radius: 4px;
    pointer-events: none;
}
.hero h1 {
    color: var(--gold-light);
    font-size: 3.2rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.hero .subtitle {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}
.hero p {
    color: #E7E1D2;
    font-size: 1.2rem;
    max-width: 680px;
    font-style: italic;
    line-height: 1.6;
}

div[data-testid="stMetric"] {
    background-color: var(--ivory);
    border: 1px solid var(--gold);
    border-left: 4px solid var(--gold);
    border-radius: 4px;
    padding: 0.8rem 1rem;
}
div[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
}
div[data-testid="stMetricValue"] {
    color: var(--navy-deep) !important;
    font-family: 'Cormorant Garamond', serif;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVIGATION STRUCTURE
# ---------------------------------------------------------
CONTENT_NAV = {
    "📊 Investment Analysis": ["Company Analysis", "Fund / ETF Analysis", "Green Bonds", "Portfolio Analysis"],
    "🌱 Sustainable Assets": ["Renewable Energy", "Green Real Estate", "EVs & Batteries", "Water", "Circular Economy"],
    "🌍 Impact": ["Carbon", "Energy", "Water", "Other Impact Metrics"],
    "📚 Research": ["ESG", "Greenwashing", "Climate Risk", "Sustainable Finance"],
}

TOOLS_NAV = {
    "🧮 Investment Tools": ["IRR Calculator", "NPV Calculator", "Carbon Pricing Calculator", "Green Project Model", "Portfolio Analyzer"],
}

DESCRIPTIONS = {
    ("📊 Investment Analysis", "Company Analysis"): "Fundamental and ESG-adjusted analysis of individual listed companies.",
    ("📊 Investment Analysis", "Fund / ETF Analysis"): "Reviews of sustainable funds, ETFs, and their underlying holdings.",
    ("📊 Investment Analysis", "Green Bonds"): "Issuance trends, credit quality, and use-of-proceeds analysis for green and sustainability-linked bonds.",
    ("📊 Investment Analysis", "Portfolio Analysis"): "Portfolio construction, factor exposure, and performance analysis through a sustainability lens.",
    ("🌱 Sustainable Assets", "Renewable Energy"): "Solar, wind, and other renewable generation assets as an investable asset class.",
    ("🌱 Sustainable Assets", "Green Real Estate"): "Energy-efficient buildings, green certifications, and sustainable property investing.",
    ("🌱 Sustainable Assets", "EVs & Batteries"): "Electric vehicles, battery technology, and the supply chains that support them.",
    ("🌱 Sustainable Assets", "Water"): "Water infrastructure, utilities, and scarcity-driven investment themes.",
    ("🌱 Sustainable Assets", "Circular Economy"): "Recycling, remanufacturing, and business models built around resource efficiency.",
    ("🌍 Impact", "Carbon"): "Carbon footprint, emissions intensity, and decarbonisation tracking.",
    ("🌍 Impact", "Energy"): "Energy use, efficiency gains, and renewable energy share metrics.",
    ("🌍 Impact", "Water"): "Water usage, withdrawal, and stewardship metrics.",
    ("🌍 Impact", "Other Impact Metrics"): "Biodiversity, waste, social, and governance impact indicators.",
    ("📚 Research", "ESG"): "Frameworks, ratings methodologies, and debates around ESG investing.",
    ("📚 Research", "Greenwashing"): "Identifying and analysing misleading sustainability claims.",
    ("📚 Research", "Climate Risk"): "Physical and transition risk analysis for portfolios and companies.",
    ("📚 Research", "Sustainable Finance"): "Policy, regulation, and the evolution of sustainable capital markets.",
}

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
_needs_reset = (
    "articles" not in st.session_state
    or (st.session_state.articles and "section" not in st.session_state.articles[0])
)
if _needs_reset:
    st.session_state.articles = [
        {
            "title": "The Rise of Green Bonds in Institutional Portfolios",
            "author": "Sustainability Editorial",
            "section": "📊 Investment Analysis",
            "sub": "Green Bonds",
            "date": datetime(2026, 8, 12),
            "image": None,
            "excerpt": "Green bond issuance keeps growing as institutional investors seek fixed income aligned with climate goals.",
            "content": "Green bonds have grown from a niche market into a core holding for many institutional fixed income portfolios. Issuers, from governments to corporates, use this market to finance renewable energy, clean transport, and efficiency projects, letting investors combine yield with measurable climate impact. Underwriting standards have matured considerably, with third-party verification of use-of-proceeds now a near-universal expectation from large asset owners.",
        },
        {
            "title": "Pricing Climate Risk into Equity Valuations",
            "author": "Sustainability Editorial",
            "section": "📚 Research",
            "sub": "Climate Risk",
            "date": datetime(2026, 7, 3),
            "image": None,
            "excerpt": "Analysts are increasingly folding physical and transition risk into discounted cash flow models.",
            "content": "As physical climate events and regulatory transition pressure intensify, equity analysts are adjusting their valuation models to account for carbon exposure, stranded-asset risk, and the long-term capital investment required for decarbonisation. The result is a widening valuation gap between companies with credible transition plans and those without.",
        },
    ]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "selected_article" not in st.session_state:
    st.session_state.selected_article = None

if "nav" not in st.session_state:
    st.session_state.nav = ("Home", None)

# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------
def clean_label(label):
    parts = label.split(" ", 1)
    return parts[1] if len(parts) > 1 else label

def go_to(section, sub=None):
    st.session_state.nav = (section, sub)
    st.session_state.selected_article = None
    st.rerun()

def calculate_npv(rate, cashflows):
    return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows))

def calculate_irr(cashflows):
    low, high = -0.99, 10.0
    npv_low = calculate_npv(low, cashflows)
    npv_high = calculate_npv(high, cashflows)
    if npv_low == 0:
        return low
    if npv_high == 0:
        return high
    if (npv_low > 0) == (npv_high > 0):
        return None  # no sign change found in range
    for _ in range(200):
        mid = (low + high) / 2
        npv_mid = calculate_npv(mid, cashflows)
        if abs(npv_mid) < 1e-6:
            return mid
        if (npv_low > 0) == (npv_mid > 0):
            low, npv_low = mid, npv_mid
        else:
            high = mid
    return mid

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🌿 Sustainability")
    st.caption("Sustainable Investment Insights")
    st.markdown("---")

    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        go_to("Home")

    for section, subs in CONTENT_NAV.items():
        with st.expander(section, expanded=(st.session_state.nav[0] == section)):
            for sub in subs:
                if st.button(sub, key=f"nav_{section}_{sub}", use_container_width=True):
                    go_to(section, sub)

    for section, subs in TOOLS_NAV.items():
        with st.expander(section, expanded=(st.session_state.nav[0] == section)):
            for sub in subs:
                if st.button(sub, key=f"nav_{section}_{sub}", use_container_width=True):
                    go_to(section, sub)

    st.markdown("---")
    if st.button("⚙️ Admin", use_container_width=True, key="nav_admin"):
        go_to("Admin")

    st.markdown("---")
    st.caption(f"{len(st.session_state.articles)} article(s) published")

# ---------------------------------------------------------
# ARTICLE CARD / DETAIL
# ---------------------------------------------------------
def render_article_card(article, index):
    with st.container(border=True):
        if article.get("image") is not None:
            st.image(article["image"], use_container_width=True)
        st.markdown(f"<span class='badge'>{article['sub']}</span>", unsafe_allow_html=True)
        st.markdown(f"### {article['title']}")
        st.caption(f"By {article['author']} · {article['date'].strftime('%d %B %Y')}")
        st.write(article["excerpt"])
        if st.button("Read full article →", key=f"open_{index}"):
            st.session_state.selected_article = index
            st.rerun()

def render_article_detail(index):
    article = st.session_state.articles[index]

    if st.button("← Back"):
        st.session_state.selected_article = None
        st.rerun()

    st.markdown(f"""
    <div class="hero">
        <div class="subtitle">{clean_label(article['section'])} · {article['sub']}</div>
        <h1>{article['title']}</h1>
        <p>By {article['author']} · {article['date'].strftime('%d %B %Y')}</p>
    </div>
    """, unsafe_allow_html=True)

    if article.get("image") is not None:
        st.image(article["image"], use_container_width=True)

    with st.container(border=True):
        st.write(article["content"])

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------
def render_home():
    st.markdown("""
    <div class="hero">
        <div class="subtitle">Sustainable Investment Insights</div>
        <h1>Sustainability</h1>
        <p>In-depth analysis on ESG investing, climate risk, and capital markets for a low-carbon economy.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Featured Analyses")
    articles_sorted = sorted(
        enumerate(st.session_state.articles), key=lambda pair: pair[1]["date"], reverse=True
    )[:3]
    if not articles_sorted:
        st.info("No articles have been published yet.")
    else:
        cols = st.columns(len(articles_sorted))
        for col, (idx, article) in zip(cols, articles_sorted):
            with col:
                render_article_card(article, idx)

# ---------------------------------------------------------
# GENERIC CATEGORY PAGE (article-driven sections)
# ---------------------------------------------------------
def render_category_page(section, sub):
    description = DESCRIPTIONS.get((section, sub), "")
    st.markdown(f"""
    <div class="hero">
        <div class="subtitle">{clean_label(section)}</div>
        <h1>{sub}</h1>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

    search = st.text_input("Search within this section", placeholder="Search by title or keyword...")

    matching = [
        (i, a) for i, a in enumerate(st.session_state.articles)
        if a["section"] == section and a["sub"] == sub
    ]
    if search:
        matching = [
            (i, a) for i, a in matching
            if search.lower() in a["title"].lower() or search.lower() in a["content"].lower()
        ]
    matching = sorted(matching, key=lambda pair: pair[1]["date"], reverse=True)

    if not matching:
        st.info("No articles have been published in this section yet. Use Admin to publish the first one.")
        return

    cols = st.columns(3)
    for pos, (idx, article) in enumerate(matching):
        with cols[pos % 3]:
            render_article_card(article, idx)

# ---------------------------------------------------------
# INVESTMENT TOOLS
# ---------------------------------------------------------
def tool_hero(sub, description):
    st.markdown(f"""
    <div class="hero">
        <div class="subtitle">Investment Tools</div>
        <h1>{sub}</h1>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

def render_irr_calculator():
    tool_hero("IRR Calculator", "Estimate the internal rate of return of a stream of cash flows.")
    with st.container(border=True):
        n_periods = st.number_input("Number of periods after year 0", min_value=1, max_value=30, value=5)
        default_df = pd.DataFrame({
            "Year": list(range(n_periods + 1)),
            "Cash Flow (€)": [-100000] + [30000] * n_periods,
        })
        edited = st.data_editor(default_df, num_rows="fixed", hide_index=True, key="irr_editor")

        if st.button("Calculate IRR"):
            cashflows = edited["Cash Flow (€)"].tolist()
            irr = calculate_irr(cashflows)
            if irr is None:
                st.error("No IRR found — cash flows need at least one sign change (a negative followed by positive values, or vice versa).")
            else:
                st.metric("Internal Rate of Return", f"{irr * 100:.2f}%")
                st.bar_chart(edited.set_index("Year")["Cash Flow (€)"])

def render_npv_calculator():
    tool_hero("NPV Calculator", "Discount a stream of cash flows back to present value.")
    with st.container(border=True):
        discount_rate = st.number_input("Discount rate (%)", min_value=0.0, max_value=100.0, value=8.0, step=0.5) / 100
        n_periods = st.number_input("Number of periods after year 0", min_value=1, max_value=30, value=5, key="npv_periods")
        default_df = pd.DataFrame({
            "Year": list(range(n_periods + 1)),
            "Cash Flow (€)": [-100000] + [30000] * n_periods,
        })
        edited = st.data_editor(default_df, num_rows="fixed", hide_index=True, key="npv_editor")

        if st.button("Calculate NPV"):
            cashflows = edited["Cash Flow (€)"].tolist()
            npv = calculate_npv(discount_rate, cashflows)
            st.metric("Net Present Value", f"€ {npv:,.0f}")
            st.bar_chart(edited.set_index("Year")["Cash Flow (€)"])

def render_carbon_pricing_calculator():
    tool_hero("Carbon Pricing Calculator", "Estimate the cost of emissions and the value of emissions reductions.")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            emissions = st.number_input("Annual emissions (tCO2e)", min_value=0.0, value=10000.0, step=100.0)
            carbon_price = st.number_input("Carbon price (€/tCO2e)", min_value=0.0, value=80.0, step=1.0)
        with col2:
            reduction_target = st.slider("Emissions reduction target (%)", 0, 100, 20)

        current_cost = emissions * carbon_price
        emissions_after = emissions * (1 - reduction_target / 100)
        cost_after = emissions_after * carbon_price
        savings = current_cost - cost_after

        m1, m2, m3 = st.columns(3)
        m1.metric("Current carbon cost", f"€ {current_cost:,.0f}")
        m2.metric("Cost after reduction", f"€ {cost_after:,.0f}")
        m3.metric("Annual savings", f"€ {savings:,.0f}")

def render_green_project_model():
    tool_hero("Green Project Model", "Model the financial return of a green infrastructure or efficiency project.")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            capex = st.number_input("Initial investment / CapEx (€)", min_value=0.0, value=500000.0, step=1000.0)
            annual_revenue = st.number_input("Annual revenue or savings (€)", min_value=0.0, value=140000.0, step=1000.0)
            annual_opex = st.number_input("Annual operating cost (€)", min_value=0.0, value=20000.0, step=1000.0)
        with col2:
            lifetime = st.number_input("Project lifetime (years)", min_value=1, max_value=50, value=10)
            discount_rate = st.number_input("Discount rate (%)", min_value=0.0, max_value=100.0, value=8.0, step=0.5) / 100

        if st.button("Run Model"):
            net_annual = annual_revenue - annual_opex
            cashflows = [-capex] + [net_annual] * int(lifetime)
            npv = calculate_npv(discount_rate, cashflows)
            irr = calculate_irr(cashflows)
            payback = capex / net_annual if net_annual > 0 else None

            m1, m2, m3 = st.columns(3)
            m1.metric("NPV", f"€ {npv:,.0f}")
            m2.metric("IRR", f"{irr * 100:.2f}%" if irr is not None else "n/a")
            m3.metric("Simple payback", f"{payback:.1f} yrs" if payback else "n/a")

            df = pd.DataFrame({"Year": list(range(int(lifetime) + 1)), "Cash Flow (€)": cashflows})
            st.bar_chart(df.set_index("Year")["Cash Flow (€)"])

def render_portfolio_analyzer():
    tool_hero("Portfolio Analyzer", "Estimate expected return and risk for a simple weighted portfolio.")
    with st.container(border=True):
        default_df = pd.DataFrame({
            "Asset": ["Green Bonds", "Renewable Energy Equity", "Broad Equity", "Cash"],
            "Weight (%)": [30.0, 30.0, 30.0, 10.0],
            "Expected Return (%)": [4.0, 9.0, 7.0, 2.0],
            "Volatility (%)": [5.0, 22.0, 15.0, 0.5],
        })
        edited = st.data_editor(default_df, num_rows="dynamic", hide_index=True, key="portfolio_editor")

        if st.button("Analyze Portfolio"):
            weights = edited["Weight (%)"].to_numpy() / 100
            total_weight = weights.sum()
            if abs(total_weight - 1) > 0.01:
                st.warning(f"Weights sum to {total_weight * 100:.1f}%, not 100%. Results are normalized.")
                weights = weights / total_weight if total_weight > 0 else weights

            returns = edited["Expected Return (%)"].to_numpy() / 100
            vols = edited["Volatility (%)"].to_numpy() / 100

            expected_return = (weights * returns).sum()
            # Simplified risk estimate assuming zero correlation between assets
            portfolio_vol = ((weights * vols) ** 2).sum() ** 0.5

            m1, m2 = st.columns(2)
            m1.metric("Expected portfolio return", f"{expected_return * 100:.2f}%")
            m2.metric("Estimated portfolio volatility", f"{portfolio_vol * 100:.2f}%")
            st.caption("Volatility assumes zero correlation between assets — a simplification for illustrative purposes.")

            alloc = pd.DataFrame({"Asset": edited["Asset"], "Weight (%)": weights * 100}).set_index("Asset")
            st.bar_chart(alloc)

TOOL_FUNCS = {
    "IRR Calculator": render_irr_calculator,
    "NPV Calculator": render_npv_calculator,
    "Carbon Pricing Calculator": render_carbon_pricing_calculator,
    "Green Project Model": render_green_project_model,
    "Portfolio Analyzer": render_portfolio_analyzer,
}

# ---------------------------------------------------------
# ADMIN
# ---------------------------------------------------------
def render_admin():
    st.markdown("## Admin")

    if not st.session_state.authenticated:
        st.markdown("Enter the admin password to manage articles.")
        with st.form("login_form"):
            pwd = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log in")
        if submitted:
            correct_pwd = st.secrets.get("ADMIN_PASSWORD", "changeme")
            if pwd == correct_pwd:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password.")
        return

    if st.button("Log out"):
        st.session_state.authenticated = False
        st.rerun()

    st.markdown("### Publish New Article")
    section_choice = st.selectbox("Section", list(CONTENT_NAV.keys()), key="admin_section_choice")

    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Title")
        author = st.text_input("Author", value="Sustainability Editorial")
        sub_choice = st.selectbox("Subsection", CONTENT_NAV[section_choice])
        image = st.file_uploader("Cover image", type=["png", "jpg", "jpeg"])
        excerpt = st.text_area("Short summary (1-2 sentences)", height=80)
        content = st.text_area("Full article content", height=250)
        submitted = st.form_submit_button("Publish Article")

    if submitted:
        if not title or not content:
            st.error("Title and content are required.")
        else:
            st.session_state.articles.append({
                "title": title,
                "author": author or "Sustainability Editorial",
                "section": section_choice,
                "sub": sub_choice,
                "date": datetime.now(),
                "image": image,
                "excerpt": excerpt or content[:150] + "...",
                "content": content,
            })
            st.success(f"'{title}' has been published under {clean_label(section_choice)} → {sub_choice}.")

    st.markdown("---")
    st.markdown("### Manage Existing Articles")
    if not st.session_state.articles:
        st.info("There are no articles yet.")
    else:
        for i, article in enumerate(st.session_state.articles):
            with st.container(border=True):
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.markdown(
                        f"**{article['title']}**  \n<span class='badge'>{article['sub']}</span> · "
                        f"{clean_label(article['section'])} · {article['date'].strftime('%d %b %Y')}",
                        unsafe_allow_html=True,
                    )
                with c2:
                    if st.button("Delete", key=f"delete_{i}"):
                        st.session_state.articles.pop(i)
                        st.rerun()

# ---------------------------------------------------------
# ROUTER
# ---------------------------------------------------------
section, sub = st.session_state.nav

if st.session_state.selected_article is not None:
    render_article_detail(st.session_state.selected_article)
elif section == "Home":
    render_home()
elif section == "Admin":
    render_admin()
elif section in TOOLS_NAV:
    if sub in TOOL_FUNCS:
        TOOL_FUNCS[sub]()
    else:
        render_home()
elif section in CONTENT_NAV:
    if sub in CONTENT_NAV[section]:
        render_category_page(section, sub)
    else:
        render_home()
else:
    render_home()

st.markdown("---")
st.caption("© 2026 Sustainability · Sustainable Investment Insights")
