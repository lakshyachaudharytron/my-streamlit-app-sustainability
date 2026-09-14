import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sustainability | Duurzame Beleggingsinzichten",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# GLOBAL STYLING — Royal Blue & Gold identity
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Lora', serif;
}

:root {
    --navy-deep: #081A3D;
    --royal-blue: #16296B;
    --royal-blue-light: #2A428C;
    --gold: #C9A24B;
    --gold-light: #E7CA82;
    --ivory: #F7F8FB;
    --text-dark: #14213D;
    --text-muted: #5A6480;
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

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: var(--gold-light);
    font-weight: 700;
    letter-spacing: 0.2px;
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

.stButton > button {
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
.stButton > button:hover {
    background-color: var(--gold-light);
    color: var(--navy-deep);
    border-color: var(--navy-deep);
}

.stTextInput > div > div > input,
.stTextArea textarea,
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
            "title": "De Opkomst van Groene Obligaties in Institutionele Portefeuilles",
            "author": "Redactie Sustainability",
            "category": "Groene Obligaties",
            "date": datetime(2026, 8, 12),
            "image": None,
            "excerpt": "De uitgifte van groene obligaties blijft groeien nu institutionele beleggers vastrentende waarden zoeken die aansluiten bij klimaatdoelstellingen.",
            "content": "Groene obligaties zijn uitgegroeid van een nichemarkt tot een kernonderdeel van veel institutionele vastrentende portefeuilles. Uitgevende instellingen, van overheden tot bedrijven, gebruiken deze markt om hernieuwbare energie, schoon vervoer en efficiëntieprojecten te financieren, terwijl beleggers rendement kunnen combineren met meetbare klimaatimpact.",
        },
        {
            "title": "Klimaatrisico Verwerken in Aandelenwaarderingen",
            "author": "Redactie Sustainability",
            "category": "Klimaatrisico",
            "date": datetime(2026, 7, 3),
            "image": None,
            "excerpt": "Analisten verwerken steeds vaker fysieke en transitierisico's in hun discounted cashflow-modellen.",
            "content": "Nu fysieke klimaatgebeurtenissen en regelgevende transitiedruk toenemen, passen aandelenanalisten hun waarderingsmodellen aan om rekening te houden met CO2-blootstelling, het risico op gestrande activa en de langetermijninvesteringen die nodig zijn voor decarbonisatie.",
        },
    ]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "selected_article" not in st.session_state:
    st.session_state.selected_article = None

CATEGORIES = [
    "ESG-beleggen",
    "Groene Obligaties",
    "Klimaatrisico",
    "Impactbeleggen",
    "Koolstofmarkten",
    "Duurzaam Bankieren",
    "Hernieuwbare Energie",
    "Beleid & Regelgeving",
]

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🌿 Sustainability")
    st.caption("Inzichten in Duurzaam Beleggen")
    st.markdown("---")
    page = st.radio("Navigatie", ["Home", "Artikelen", "Beheer"], label_visibility="collapsed")
    st.markdown("---")
    st.caption(f"{len(st.session_state.articles)} artikel(en) gepubliceerd")

# ---------------------------------------------------------
# HELPER: ARTIKELKAART (klik -> eigen artikelpagina)
# ---------------------------------------------------------
def render_article_card(article, index):
    with st.container(border=True):
        if article.get("image") is not None:
            st.image(article["image"], use_container_width=True)
        st.markdown(f"<span class='badge'>{article['category']}</span>", unsafe_allow_html=True)
        st.markdown(f"### {article['title']}")
        st.caption(f"Door {article['author']} · {article['date'].strftime('%d %B %Y')}")
        st.write(article["excerpt"])
        if st.button("Lees volledig artikel →", key=f"open_{index}"):
            st.session_state.selected_article = index
            st.rerun()

# ---------------------------------------------------------
# ARTIKELPAGINA
# ---------------------------------------------------------
def render_article_detail(index):
    article = st.session_state.articles[index]

    if st.button("← Terug"):
        st.session_state.selected_article = None
        st.rerun()

    st.markdown(f"""
    <div class="hero">
        <div class="subtitle">{article['category']}</div>
        <h1>{article['title']}</h1>
        <p>Door {article['author']} · {article['date'].strftime('%d %B %Y')}</p>
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
        <div class="subtitle">Duurzame Beleggingsinzichten</div>
        <h1>Sustainability</h1>
        <p>Gedegen analyses over ESG-beleggen, klimaatrisico en kapitaalmarkten voor een koolstofarme economie.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Gepubliceerde artikelen", len(st.session_state.articles))
    col2.metric(
        "Categorieën",
        len(set(a["category"] for a in st.session_state.articles)) if st.session_state.articles else 0,
    )
    col3.metric(
        "Laatste update",
        max((a["date"] for a in st.session_state.articles), default=datetime.now()).strftime("%d %b %Y"),
    )

    st.markdown("### Uitgelichte Analyses")
    articles_sorted = sorted(
        enumerate(st.session_state.articles), key=lambda pair: pair[1]["date"], reverse=True
    )[:3]
    if not articles_sorted:
        st.info("Er zijn nog geen artikelen gepubliceerd.")
    else:
        cols = st.columns(len(articles_sorted))
        for col, (idx, article) in zip(cols, articles_sorted):
            with col:
                render_article_card(article, idx)

# ---------------------------------------------------------
# ARTIKELEN
# ---------------------------------------------------------
def render_articles():
    st.markdown("## Onderzoek & Artikelen")
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("Zoek artikelen", placeholder="Zoek op titel of trefwoord...")
    with col2:
        filter_category = st.selectbox("Filter op categorie", ["Alle"] + CATEGORIES)

    indexed = list(enumerate(st.session_state.articles))

    if search:
        indexed = [
            (i, a) for i, a in indexed
            if search.lower() in a["title"].lower() or search.lower() in a["content"].lower()
        ]
    if filter_category != "Alle":
        indexed = [(i, a) for i, a in indexed if a["category"] == filter_category]

    indexed = sorted(indexed, key=lambda pair: pair[1]["date"], reverse=True)

    if not indexed:
        st.info("Geen artikelen gevonden voor deze zoekopdracht.")
        return

    cols = st.columns(3)
    for pos, (idx, article) in enumerate(indexed):
        with cols[pos % 3]:
            render_article_card(article, idx)

# ---------------------------------------------------------
# BEHEER (ADMIN)
# ---------------------------------------------------------
def render_admin():
    st.markdown("## Beheer")

    if not st.session_state.authenticated:
        st.markdown("Voer het beheerderswachtwoord in om artikelen te beheren.")
        with st.form("login_form"):
            pwd = st.text_input("Wachtwoord", type="password")
            submitted = st.form_submit_button("Inloggen")
        if submitted:
            correct_pwd = st.secrets.get("ADMIN_PASSWORD", "changeme")
            if pwd == correct_pwd:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Onjuist wachtwoord.")
        return

    if st.button("Uitloggen"):
        st.session_state.authenticated = False
        st.rerun()

    st.markdown("### Nieuw Artikel Publiceren")
    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Titel")
        author = st.text_input("Auteur", value="Redactie Sustainability")
        category = st.selectbox("Categorie", CATEGORIES)
        image = st.file_uploader("Coverafbeelding", type=["png", "jpg", "jpeg"])
        excerpt = st.text_area("Korte samenvatting (1-2 zinnen)", height=80)
        content = st.text_area("Volledige inhoud van het artikel", height=250)
        submitted = st.form_submit_button("Publiceer Artikel")

    if submitted:
        if not title or not content:
            st.error("Titel en inhoud zijn verplicht.")
        else:
            st.session_state.articles.append({
                "title": title,
                "author": author or "Redactie Sustainability",
                "category": category,
                "date": datetime.now(),
                "image": image,
                "excerpt": excerpt or content[:150] + "...",
                "content": content,
            })
            st.success(f"'{title}' is gepubliceerd.")

    st.markdown("---")
    st.markdown("### Bestaande Artikelen Beheren")
    if not st.session_state.articles:
        st.info("Er zijn nog geen artikelen.")
    else:
        for i, article in enumerate(st.session_state.articles):
            with st.container(border=True):
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.markdown(
                        f"**{article['title']}**  \n<span class='badge'>{article['category']}</span> · "
                        f"{article['date'].strftime('%d %b %Y')}",
                        unsafe_allow_html=True,
                    )
                with c2:
                    if st.button("Verwijderen", key=f"delete_{i}"):
                        st.session_state.articles.pop(i)
                        st.rerun()

# ---------------------------------------------------------
# ROUTER
# ---------------------------------------------------------
if st.session_state.selected_article is not None:
    render_article_detail(st.session_state.selected_article)
elif page == "Home":
    render_home()
elif page == "Artikelen":
    render_articles()
elif page == "Beheer":
    render_admin()

st.markdown("---")
st.caption("© 2026 Sustainability · Inzichten in Duurzaam Beleggen")
