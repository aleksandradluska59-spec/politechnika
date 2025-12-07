import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Konfiguracja strony Streamlit
st.set_page_config(layout="centered")
st.title("🎅 Interaktywny Święty Mikołaj (Streamlit)")
st.write("Użyj suwaka poniżej, aby zmienić kolor czapki Mikołaja.")

# Lista kolorów do wyboru dla czapki
kolory_czapek = {
    0: '#B22222',  # Czerwony (tradycyjny)
    1: '#1E90FF',  # Niebieski
    2: '#3CB371',  # Zielony
    3: '#8A2BE2'   # Fioletowy
}
opis_kolorow = {
    0: "Czerwony (Tradycyjny)",
    1: "Niebieski (Morski)",
    2: "Zielony (Leśny)",
    3: "Fioletowy (Ametystowy)"
}

# --- Widżet sterujący ---
# Używamy st.slider do pobrania indeksu koloru
kolor_indeks = st.slider(
    'Wybierz kolor czapki',
    min_value=0,
    max_value=3,
    step=1,
    value=0,
    format='Kolor: %d'
)

# Wyświetlanie nazwy wybranego koloru
st.info(f"Aktualnie wybrany kolor: **{opis_kolorow[kolor_indeks]}**")


# Funkcja rysująca Mikołaja
def rysuj_mikolaja(kolor_indeks):
    """Rysuje Mikołaja z tułowiem, rękami, prezentami i czapką o zmiennym kolorze."""

    kolor_czapki = kolory_czapek[kolor_indeks]

    # Ustawienie wykresu
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-15, 10)
    ax.axis('off')

    # --- Twarz ---
    ax.add_patch(patches.Circle((0, -0.5), 3.0, color='#FAD7A0', zorder=10)) # Skóra

    # Oczy
    ax.add_patch(patches.Circle((-1.2, 0.5), 0.3, color='black', zorder=11))
    ax.add_patch(patches.Circle((1.2, 0.5), 0.3, color='black', zorder=11))

    # Nos
    ax.add_patch(patches.Circle((0, -0.8), 0.7, color='red', zorder=12))

    # Wąsy
    ax.add_patch(patches.Ellipse((-2, -2), 3, 2, angle=30, color='white', zorder=13))
    ax.add_patch(patches.Ellipse((2, -2), 3, 2, angle=-30, color='white', zorder=13))

    # --- Broda ---
    ax.add_patch(patches.Ellipse((0, -4.5), 7, 7, color='white', zorder=9))
    ax.add_patch(patches.Circle((-2.5, -4), 2, color='white', zorder=9))
    ax.add_patch(patches.Circle((2.5, -4), 2, color='white', zorder=9))
    ax.add_patch(patches.Circle((0, -6.5), 2.5, color='white', zorder=9))
    ax.add_patch(patches.Circle((0, -0.5), 3.0, color='#FAD7A0', zorder=10)) # Zakrycie

    # --- Tułów ---
    ax.add_patch(patches.Rectangle((-4.5, -10), 9, 8, color='#B22222', zorder=8)) # Kurtka

    # --- Pasek ---
    ax.add_patch(patches.Rectangle((-5, -6), 10, 1.5, color='black', zorder=15))
    ax.add_patch(patches.Rectangle((-1.5, -6.25), 3, 2, color='gold', zorder=16)) # Klamra

    # --- Ręce ---
    ax.add_patch(patches.Ellipse((-5.5, -4.5), 3, 4, angle=45, color='#B22222', zorder=7))
    ax.add_patch(patches.Ellipse((5.5, -4.5), 3, 4, angle=-45, color='#B22222', zorder=7))
    ax.add_patch(patches.Circle((-7, -3), 1.5, color='black', zorder=14))
    ax.add_patch(patches.Circle((7, -3), 1.5, color='black', zorder=14))

    # --- Nogi i Buty ---
    ax.add_patch(patches.Rectangle((-3, -13), 2.5, 3, color='#B22222', zorder=7))
    ax.add_patch(patches.Rectangle((0.5, -13), 2.5, 3, color='#B22222', zorder=7))
    ax.add_patch(patches.Rectangle((-4, -15), 4, 2, color='black', zorder=17))
    ax.add_patch(patches.Rectangle((0, -15), 4, 2, color='black', zorder=17))

    # --- Czapka (Interaktywna) ---
    ax.fill([-4, 4, 0, -4], [0, 0, 6, 0], color=kolor_czapki, zorder=18)
    ax.add_patch(patches.Rectangle((-4.5, -0.5), 9, 1.0, color='white', zorder=19))
    ax.add_patch(patches.Circle((0, 6.0), 1.0, color='white', zorder=20))

    # --- Prezenty ---
    ax.add_patch(patches.Rectangle((-9, -13), 3, 3, color='green', zorder=5))
    ax.add_patch(patches.Rectangle((-8, -10), 2.5, 2.5, color='blue', zorder=6))
    ax.add_patch(patches.Rectangle((-9.5, -10), 2, 2, color='yellow', zorder=4))

    ax.add_patch(patches.Rectangle((6, -13), 3, 3, color='red', zorder=5))
    ax.add_patch(patches.Rectangle((6.5, -10), 2.5, 2.5, color='gold', zorder=6))
    ax.add_patch(patches.Rectangle((5, -10), 2, 2, color='lime', zorder=4))

    return fig

# --- Wywołanie funkcji i wyświetlenie w Streamlit ---
mikolaj_figura = rysuj_mikolaja(kolor_indeks)

# Używamy st.pyplot, aby wyświetlić figurę Matplotlib
st.pyplot(mikolaj_figura)
