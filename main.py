Import json
import streamlit as st


# Funcție pentru citirea datelor din fișierul JSON
def load_movies(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Funcție pentru recomandarea filmelor
def recommend_movies(movies, preferred_genres):
    recommendations = []
    for movie in movies:
        if any(genre in preferred_genres for genre in movie["genre"]):
            recommendations.append(movie["title"])
    return recommendations


# Funcție principală pentru interfața utilizator
def main():
    st.title("Recomandări de Filme 🎬")

    # Încărcarea filmelor din fișierul JSON
    movies = load_movies("movies.json")

    # Introducerea numelui utilizatorului
    name = st.text_input("Introduceți numele dvs.:")

    # Selectarea genurilor preferate
    genres = ["Action", "Drama", "Sci-Fi", "Thriller", "Crime", "Comedy", "Horror"]
    preferred_genres = st.multiselect("Selectați genurile preferate:", genres)

    # Afișarea recomandărilor
    if st.button("Sugerează filme"):
        if name and preferred_genres:
            recommendations = recommend_movies(movies, preferred_genres)
            if recommendations:
                st.write(f"Filme recomandate pentru {name}:")
                for movie in recommendations:
                    st.write(f"- {movie}")
            else:
                st.write("Nu există filme care să corespundă genurilor selectate.")
        else:
            st.write("Vă rugăm să completați toate câmpurile.")


if __name__ == "__main__":
    main()
