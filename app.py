from pathlib import Path

import streamlit as st


STATIC_DIR = Path(__file__).resolve().parent / "static"
st.set_page_config(page_title="Sosyal Medya Duvarı", page_icon="✎")
st.html("""
<style>
:root {
    --ink: #22272e;
    --muted: #525d68;
    --paper: #f7f5ef;
    --line: #d9d9d1;
}
.stApp, [data-testid="stHeader"] { background: var(--paper); }
[data-testid="stAppViewContainer"] .block-container {
    max-width: 820px;
    padding: 3.1rem 1.1rem 2rem;
}
[data-testid="stToolbar"], #MainMenu, footer { visibility: hidden; }
.gallery-header h1 {
    color: var(--ink);
    font: 600 clamp(2.35rem, 7vw, 4.5rem)/1.07 Georgia, serif;
    letter-spacing: -.055em;
    padding: 0;
    margin: 0;
}
.photo-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: .75rem;
}
.photo-card {
    display: block;
    position: relative;
    box-sizing: border-box;
    width: 100%;
    min-width: 0;
    align-self: start;
    aspect-ratio: 1 / 1;
    color: var(--ink) !important;
    background: #fff;
    text-decoration: none !important;
    border: 1px solid var(--line);
    border-radius: .8rem;
    overflow: hidden;
}
.photo-card img {
    display: block;
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: #ebe9e0;
}
.photo-card:hover, .photo-card:focus-visible,
.gallery-nav a:hover, .gallery-nav a:focus-visible, .back-link:focus-visible {
    outline: 2px solid #31596d;
    outline-offset: 2px;
}
.gallery-nav {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: .45rem;
    align-items: center;
    text-align: center;
    color: var(--muted);
    font-size: .85rem;
    font-variant-numeric: tabular-nums;
}
.gallery-nav a, .gallery-nav .disabled, .back-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: .35rem .6rem;
    border-radius: .55rem;
    text-decoration: none !important;
    font-weight: 600;
}
.gallery-nav a { background: #263743; color: #fff !important; }
.gallery-nav .disabled { color: #57616a; background: #e7e5de; }
.back-link { color: var(--ink) !important; border: 1px solid var(--line); }
.full-photo { display: block; width: 100%; height: auto; border-radius: .65rem; }
@media (max-width: 580px) {
    [data-testid="stAppViewContainer"] .block-container { padding: 2.75rem .85rem 1.5rem; }
    .photo-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .55rem; }
}
</style>
""")


def photo_link(number):
    return f"?foto={number}"


def navigation(current, total):
    previous = (
        f'<a href="{photo_link(current - 1)}" rel="prev">‹ Önceki</a>'
        if current > 1 else '<span class="disabled" aria-disabled="true">‹ Önceki</span>'
    )
    following = (
        f'<a href="{photo_link(current + 1)}" rel="next">Sonraki ›</a>'
        if current < total else '<span class="disabled" aria-disabled="true">Sonraki ›</span>'
    )
    st.html('<nav class="gallery-nav" aria-label="Fotoğraflar">'
            f'{previous}<span>{current} / {total}</span>{following}</nav>')


def show_grid(photos):
    cards = []
    for number, filename in enumerate(photos, start=1):
        cards.append(
            f'<a class="photo-card" href="{photo_link(number)}" '
            f'aria-label="{number}. fotoğrafı aç">'
            f'<img src="./app/static/thumbs/{filename}?v=2" alt="" '
            'loading="lazy" decoding="async"></a>'
        )
    st.html('<div class="photo-grid">' + "".join(cards) + '</div>')


def show_photo(photos, number):
    st.html('<a class="back-link" href="?">‹ Galeriye dön</a>')
    navigation(number, len(photos))
    filename = photos[number - 1]
    st.html(f'<img class="full-photo" src="./app/static/photos/{filename}?v=2" '
            f'alt="{number}. fotoğraf" decoding="async">')


def main():
    photos = sorted(
        path.name for path in (STATIC_DIR / "photos").glob("photo-[0-9][0-9][0-9].jpg")
        if (STATIC_DIR / "thumbs" / path.name).is_file()
    )
    st.html('<header class="gallery-header"><h1>Sosyal Medya Duvarı</h1></header>')
    if not photos:
        st.info("Galeriye henüz fotoğraf eklenmedi.")
        return

    try:
        selected = int(st.query_params.get("foto", "0"))
    except ValueError:
        selected = 0

    if 1 <= selected <= len(photos):
        show_photo(photos, selected)
    else:
        show_grid(photos)


main()
