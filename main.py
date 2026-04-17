import streamlit as st

st.set_page_config(layout="wide", page_title="FitSync", page_icon="💪")

THEMES = {
    ("dark",  "Midnight"): {"bg":"#0a0a14","text":"#f1f5f9","muted":"rgba(255,255,255,0.42)","logo":"#a5b4fc","badge_bg":"rgba(99,102,241,0.18)","badge_c":"#a5b4fc","cta":"#4f46e5","ghost_c":"rgba(255,255,255,0.5)","ghost_b":"rgba(255,255,255,0.12)","div":"rgba(255,255,255,0.08)","sub":"rgba(255,255,255,0.38)"},
    ("dark",  "Aurora"):   {"bg":"#020c14","text":"#e2f4ef","muted":"rgba(180,240,220,0.45)","logo":"#5dcaa5","badge_bg":"rgba(29,158,117,0.2)","badge_c":"#5dcaa5","cta":"#1d9e75","ghost_c":"rgba(180,240,220,0.5)","ghost_b":"rgba(93,202,165,0.2)","div":"rgba(93,202,165,0.12)","sub":"rgba(180,240,220,0.38)"},
    ("dark",  "Rose"):     {"bg":"#0f070d","text":"#fce7f3","muted":"rgba(252,231,243,0.4)","logo":"#ed93b1","badge_bg":"rgba(212,83,126,0.18)","badge_c":"#ed93b1","cta":"#d4537e","ghost_c":"rgba(252,231,243,0.45)","ghost_b":"rgba(212,83,126,0.2)","div":"rgba(212,83,126,0.12)","sub":"rgba(252,231,243,0.38)"},
    ("light", "Midnight"): {"bg":"#f0f0ff","text":"#1e1b4b","muted":"#6366f1","logo":"#4f46e5","badge_bg":"#ede9fe","badge_c":"#4338ca","cta":"#4f46e5","ghost_c":"#6366f1","ghost_b":"#c7d2fe","div":"#c7d2fe","sub":"#818cf8"},
    ("light", "Aurora"):   {"bg":"#f0fdf8","text":"#064e3b","muted":"#1d9e75","logo":"#0f6e56","badge_bg":"#e1f5ee","badge_c":"#085041","cta":"#0f6e56","ghost_c":"#1d9e75","ghost_b":"#9fe1cb","div":"#9fe1cb","sub":"#5dcaa5"},
    ("light", "Rose"):     {"bg":"#fff0f6","text":"#4b1528","muted":"#d4537e","logo":"#993556","badge_bg":"#fbeaf0","badge_c":"#72243e","cta":"#993556","ghost_c":"#d4537e","ghost_b":"#f4c0d1","div":"#f4c0d1","sub":"#ed93b1"},
}

if "mode"  not in st.session_state: st.session_state.mode  = "dark"
if "theme" not in st.session_state: st.session_state.theme = "Midnight"

# ── Sidebar controls ──────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding: 8px 0 20px;">
        <div style="font-size:18px; font-weight:700; margin-bottom:4px;">⚡ FitSync</div>
        <div style="font-size:12px; opacity:0.5;">Settings</div>
    </div>
    <hr style="border:none; border-top:1px solid rgba(255,255,255,0.08); margin-bottom:20px;">
    <div style="font-size:12px; font-weight:500; opacity:0.5; letter-spacing:0.05em; margin-bottom:10px;">APPEARANCE</div>
    """, unsafe_allow_html=True)

    chosen_theme = st.selectbox(
        "🎨 Theme",
        ["Midnight", "Aurora", "Rose"],
        index=["Midnight", "Aurora", "Rose"].index(st.session_state.theme)
    )
    if chosen_theme != st.session_state.theme:
        st.session_state.theme = chosen_theme
        st.rerun()

    st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

    chosen_mode = st.radio(
        "🌗 Mode",
        ["Dark", "Light"],
        index=0 if st.session_state.mode == "dark" else 1,
        horizontal=True
    )
    if chosen_mode.lower() != st.session_state.mode:
        st.session_state.mode = chosen_mode.lower()
        st.rerun()

    st.markdown("""
    <hr style="border:none; border-top:1px solid rgba(255,255,255,0.08); margin:24px 0 16px;">
    <div style="font-size:12px; font-weight:500; opacity:0.5; letter-spacing:0.05em; margin-bottom:10px;">NAVIGATE</div>
    """, unsafe_allow_html=True)

t = THEMES[(st.session_state.mode, st.session_state.theme)]

# ── Page styles ───────────────────────────────────
st.markdown(f"""
<style>
.stApp, [data-testid="stAppViewContainer"] {{
    background: {t['bg']} !important;
    font-family: 'Segoe UI', sans-serif;
}}
[data-testid="stHeader"]  {{ display: none !important; }}
[data-testid="stToolbar"] {{ display: none !important; }}
footer {{ display: none !important; }}
.block-container {{
    padding: 0 !important;
    max-width: 100% !important;
}}
[data-testid="stVerticalBlock"] {{ gap: 0 !important; }}

/* Sidebar styling */
[data-testid="stSidebar"] {{
    background: #0d0d1a !important;
    border-right: 1px solid {t['div']} !important;
}}
[data-testid="stSidebar"] * {{
    color: {t['text']} !important;
}}

/* Hero */
.hero-wrap {{
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 40px 40px 60px;
    color: {t['text']};
    width: 100%;
    box-sizing: border-box;
}}
.badge {{
    display: inline-block;
    background: {t['badge_bg']};
    color: {t['badge_c']};
    font-size: 11px;
    font-weight: 500;
    padding: 5px 16px;
    border-radius: 999px;
    letter-spacing: 0.06em;
    margin-bottom: 24px;
}}
.hero-wrap h1 {{
    font-size: 52px;
    font-weight: 700;
    color: {t['text']};
    margin: 0 0 18px;
    line-height: 1.12;
}}
.hero-wrap p {{
    font-size: 17px;
    color: {t['muted']};
    max-width: 460px;
    margin: 0 auto 40px;
    line-height: 1.75;
}}
.hero-btns {{
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 56px;
}}
.btn-cta {{
    background: {t['cta']};
    color: #fff;
    border: none;
    font-size: 16px;
    font-weight: 600;
    padding: 15px 40px;
    border-radius: 14px;
    cursor: pointer;
    font-family: 'Segoe UI', sans-serif;
}}
.btn-ghost {{
    background: transparent;
    color: {t['ghost_c']};
    border: 1px solid {t['ghost_b']};
    font-size: 16px;
    font-weight: 500;
    padding: 15px 40px;
    border-radius: 14px;
    cursor: pointer;
    font-family: 'Segoe UI', sans-serif;
}}
.features {{
    display: flex;
    gap: 60px;
    justify-content: center;
    flex-wrap: wrap;
    padding-top: 36px;
    border-top: 1px solid {t['div']};
    width: 100%;
    max-width: 520px;
}}
.feat-icon  {{ font-size: 26px; margin-bottom: 10px; }}
.feat-label {{ font-size: 15px; font-weight: 600; color: {t['text']}; }}
.feat-sub   {{ font-size: 13px; color: {t['sub']}; margin-top: 4px; }}
</style>

<div class="hero-wrap">
    <div class="badge">✦ Your fitness companion</div>
    <h1>Welcome to FitSync 💪</h1>
    <p>Track your steps, sleep, and recovery in one place.<br>Build better habits — one day at a time.</p>
    <div class="hero-btns">
    <a href="/Dashboard" class="btn-cta">🚀 Go to Dashboard →</a>
    <a href="/Trends" class="btn-ghost">📈 View Trends</a>
</div>
    <div class="features">
        <div class="feat">
            <div class="feat-icon">🚶</div>
            <div class="feat-label">Steps</div>
            <div class="feat-sub">Daily tracking</div>
        </div>
        <div class="feat">
            <div class="feat-icon">🌙</div>
            <div class="feat-label">Sleep</div>
            <div class="feat-sub">Hours & quality</div>
        </div>
        <div class="feat">
            <div class="feat-icon">❤️</div>
            <div class="feat-label">Recovery</div>
            <div class="feat-sub">Score & trends</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)