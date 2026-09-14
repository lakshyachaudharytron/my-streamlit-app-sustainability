import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sustainability",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# GLOBAL STYLING
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

:root {
    --forest-dark: #1B4332;
    --forest: #2D6A4F;
    --forest-light: #40916C;
    --mint: #95D5B2;
    --bg: #F7F9F7;
    --text-muted: #5C6B66;
}

.stApp {
    background-color: var(--bg);
}

section[data-testid="stSidebar"] {
    background-color: var(--forest-dark);
}
section[data-testid="stSidebar"] * {
    color: #F0F5F2 !important;
}

h1, h2, h3 {
    color: var(--forest-dark);
    font-weight: 700;
}

.stButton > button {
    background-color: var(--forest);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1.3rem;
    font-weight: 600;
    transition: background-color 0.2s ease;
}
.stButton > button:hover {
    background-color: var(--forest-dark);
    color: white;
}

.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div {
    border-radius: 8px !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px !important;
}

.badge {
    display: inline-block;
    background-color: var(--mint);
    color: var(--forest-dark);
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}

.hero {
    padding: 3rem 2rem;
    border-radius: 16px;
    background: linear-gradient(135deg, var(--forest-dark), var(--forest));
    color: white;
    margin-bottom: 2rem;
}
.hero h1 {
    color: white;
    font-size: 2.6rem;
    margin-bottom: 0.5rem;
}
.hero p {
    color: #E4F0EA;
    font-size: 1.1rem;
    max-width: 650px;
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
            "title": "The Rise of Circular Economies",
            "author": "Sustainability Team",
            "category": "Circular Economy",
            "date": datetime(2026, 8, 12),
            "image": None,
            "excerpt": "How businesses are redesigning supply chains to eliminate waste and keep resources in use for longer.",
            "content": "Circular economy models are reshaping how companies think about product lifecycles. Instead of the traditional take-make-dispose approach, organizations are now designing for reuse, repair, and recycling from the outset.",
        },
        {
            "title": "Renewable Energy Adoption in 2026",
            "author": "Sustainability Team",
            "category": "Energy",
            "date": datetime(2026, 7, 3),
            "image": None,
            "excerpt": "A look at how solar and wind capacity additions are accelerating the global energy transition.",
            "content": "Global renewable capacity has continued its rapid expansion, driven by falling technology costs and supportive policy frameworks.",
        },
    ]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

CATEGORIES = ["Climate", "Energy", "Circular Economy", "Biodiversity", "Sustainable Living", "Policy", "Corporate ESG"]

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🌱 Sustainability")
    st.caption("Insights for a greener future")
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
        <h1>Sustainability</h1>
        <p>Stories, research, and insights on climate, energy, and building a more sustainable future.</p>
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

    st.markdown("### Latest Articles")
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
    st.markdown("## Articles")
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

    st.markdown("### Upload a New Article")
    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Title")
        author = st.text_input("Author", value="Sustainability Team")
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
                "author": author or "Sustainability Team",
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
st.caption("© 2026 Sustainability · Built with Streamlit")
