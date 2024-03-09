import pickle
import streamlit as st
import requests
import asyncio
import aiohttp

async def fetch_poster(session, movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    async with session.get(url) as response:
        data = await response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None

async def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            tasks.append(fetch_poster(session, movie_id))
        recommended_movie_posters = await asyncio.gather(*tasks)
        recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies, recommended_movie_posters

def main():
    st.header('Movie Recommender System')
    movies = pickle.load(open('model/movie_list.pkl','rb'))
    similarity = pickle.load(open('model/similarity.pkl','rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendations'):
        recommended_movie_names, recommended_movie_posters = asyncio.run(recommend(selected_movie, movies, similarity))
        col1, col2, col3, col4, col5 = st.beta_columns(5)
        for i in range(len(recommended_movie_names)):
            with col1:
                st.text(recommended_movie_names[i])
                if recommended_movie_posters[i]:
                    st.image(recommended_movie_posters[i])

if __name__ == "__main__":
    main()

