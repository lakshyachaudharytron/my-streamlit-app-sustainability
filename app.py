import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sustainability | Sustainable Finance Insights",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# GLOBAL STYLING — "Royal" emerald & gold identity
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Lora', serif;
}

:root {
    --emerald-deep: #0B3D2E;
    --emerald: #14532D;
    --emerald-light: #2E7D5B;
    --gold: #C9A24B;
    --gold-light: #E4C77E;
    --ivory: #FAF7F0;
    --charcoal: #26302B;
    --text-muted: #6B7268;
}

.stApp {
    background-color: var(--ivory);
}

section[data-testid="stSidebar"] {
    background-color: var(--emerald-deep);
    border-right: 1px solid var(--gold);
}
section[data-testid="stSidebar"] * {
    color: #F3EFE3 !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-family: 'Lora', serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: var(--emerald-deep);
    font-weight: 700;
    letter-spacing: 0.2px;
}

hr {
    border-top: 1px solid var(--gold-light) !important;
}

.stButton > button {
    background-color: var(--emerald-deep);
    color: var(--gold-light);
    border: 1px solid var(--gold);
    border-radius: 4px;
    padding: 0.55rem 1.4rem;
    font-family: 'Lora', serif;
    font-weight: 600;
    letter-spacing: 0.4px;
    transition: all 0.25s ease;
}
.stButton > button:hover {
    background-color: var(--gold);
    color: var(--emerald-deep);
    border-color: var(--emerald-deep);
}

.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div {
    border-radius: 4px !important;
    border: 1px solid #D8CFB8 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 6px !important;
    border: 1px solid #E3DCC8 !important;
}

.badge {
    display: inline-block;
    background-color: var(--emerald-deep);
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
    background: linear-gradient(135deg, var(--emerald-deep) 0%, var(--emerald) 100%);
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
    font-size: 2.8rem;
    margin-bottom: 0.6rem;
}
.hero .subtitle {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}
.hero p {
    color: #E9E4D4;
    font-size: 1.1rem;
    max-width: 680px;
    font-style: italic;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E3DCC8;
    border-left: 3px solid var(--gold);
    border-radius: 4px;
    padding: 0.8rem 1rem;
}
div[data-testid="stMetricLabel"] {
    color: var(--text-muted);
}
div[data-testid="stMetricValue"] {
    color: var(--emerald-deep);
    font-family: 'Playfair Display', serif;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "articles" not in st.session_state:
    st.session_state.articles = [
        {
            "title": "The Growth of Green Bonds in Institutional Portfolios",
            "author": "Sustainability Desk",
            "category": "Green Bonds",
            "date": datetime(2026, 8, 12),
            "image": None,
            "excerpt": "Green bond issuance continues to climb as institutional investors seek fixed-income exposure aligned with climate mandates.",
            "content": "Green bonds have moved from a niche instrument to a core allocation within many institutional fixed-income portfolios. Issuers ranging from sovereigns to corporates are tapping this market to fund renewable energy, clean transport, and efficiency projects, while investors gain a way to align yield-seeking capital with measurable climate outcomes.",
        },
        {
            "title": "Pricing Climate Risk into Equity Valuations",
            "author": "Sustainability Desk",
            "category": "Climate Risk",
            "date": datetime(2026, 7, 3),
            "image": None,
            "excerpt": "Analysts are increasingly incorporating physical and transition climate risk into discounted cash flow models.",
            "content": "As physical climate events and regulatory transition pressures intensify, equity analysts are adjusting valuation models to reflect carbon exposure, stranded-asset risk, and long-term capital expenditure shifts required for decarbonization.",
        },
    ]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

CATEGORIES = [
    "ESG Investing",
    "Green Bonds",
    "Climate Risk",
    "Impact Investing",
    "Carbon Markets",
    "Sustainable Banking",
    "Renewable Energy Finance",
    "Policy & Regulation",
]

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🌿 Sustainability")
    st.caption("Sustainable Finance & Investment Intelligence")
    st.markdown("---")
    page = st.radio("Navigate", ["Home", "Articles", "Admin"], label_visibility="collapsed")
    st.markdown("---")
    st.caption(f"{len(st.session_state.articles)} article(s) published")

# ---------------------------------------------------------
# HELPER: ARTICLE CARD
# ---------------------------------------------------------
def render_article_card(article):
    with st.container(border=True):
        if article.get("image") is not None:
            st.image(article["image"], use_container_width=True)
        st.markdown(f"<span class='badge'>{article['category']}</span>", unsafe_allow_html=True)
        st.markdown(f"### {article['title']}")
        st.caption(f"By {article['author']} · {article['date'].strftime('%B %d, %Y')}")
        st.write(article["excerpt"])
        with st.expander("Read full article"):
            st.write(article["content"])

# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------
def render_home():
    st.markdown("""
    <div class="hero">
        <div class="subtitle">Sustainable Finance Intelligence</div>
        <h1>Sustainability</h1>
        <p>Rigorous analysis on ESG investing, climate risk, and capital markets built for a low-carbon economy.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Articles Published", len(st.session_state.articles))
    col2.metric(
        "Categories Covered",
        len(set(a["category"] for a in st.session_state.articles)) if st.session_state.articles else 0,
    )
    col3.metric(
        "Latest Update",
        max((a["date"] for a in st.session_state.articles), default=datetime.now()).strftime("%b %d, %Y"),
    )

    st.markdown("### Featured Analysis")
    latest = sorted(st.session_state.articles, key=lambda a: a["date"], reverse=True)[:3]
    if not latest:
        st.info("No articles published yet.")
    else:
        cols = st.columns(len(latest))
        for col, article in zip(cols, latest):
            with col:
                render_article_card(article)

# ---------------------------------------------------------
# ARTICLES PAGE
# ---------------------------------------------------------
def render_articles():
    st.markdown("## Research & Articles")
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("Search articles", placeholder="Search by title or keyword...")
    with col2:
        filter_category = st.selectbox("Filter by category", ["All"] + CATEGORIES)

    filtered = st.session_state.articles
    if search:
        filtered = [
            a for a in filtered
            if search.lower() in a["title"].lower() or search.lower() in a["content"].lower()
        ]
    if filter_category != "All":
        filtered = [a for a in filtered if a["category"] == filter_category]

    filtered = sorted(filtered, key=lambda a: a["date"], reverse=True)

    if not filtered:
        st.info("No articles match your search.")
        return

    cols = st.columns(3)
    for i, article in enumerate(filtered):
        with cols[i % 3]:
            render_article_card(article)

# ---------------------------------------------------------
# ADMIN PAGE
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

    st.markdown("### Publish a New Article")
    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Title")
        author = st.text_input("Author", value="Sustainability Desk")
        category = st.selectbox("Category", CATEGORIES)
        image = st.file_uploader("Cover image", type=["png", "jpg", "jpeg"])
        excerpt = st.text_area("Short excerpt (1-2 sentences)", height=80)
        content = st.text_area("Full article content", height=250)
        submitted = st.form_submit_button("Publish Article")

    if submitted:
        if not title or not content:
            st.error("Title and content are required.")
        else:
            st.session_state.articles.append({
                "title": title,
                "author": author or "Sustainability Desk",
                "category": category,
                "date": datetime.now(),
                "image": image,
                "excerpt": excerpt or content[:150] + "...",
                "content": content,
            })
            st.success(f"'{title}' published.")

    st.markdown("---")
    st.markdown("### Manage Existing Articles")
    if not st.session_state.articles:
        st.info("No articles yet.")
    else:
        for i, article in enumerate(st.session_state.articles):
            with st.container(border=True):
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.markdown(
                        f"**{article['title']}**  \n<span class='badge'>{article['category']}</span> · "
                        f"{article['date'].strftime('%b %d, %Y')}",
                        unsafe_allow_html=True,
                    )
                with c2:
                    if st.button("Delete", key=f"delete_{i}"):
                        st.session_state.articles.pop(i)
                        st.rerun()

# ---------------------------------------------------------
# ROUTER
# ---------------------------------------------------------
if page == "Home":
    render_home()
elif page == "Articles":
    render_articles()
elif page == "Admin":
    render_admin()

st.markdown("---")
st.caption("© 2026 Sustainability · Sustainable Finance Intelligence")
