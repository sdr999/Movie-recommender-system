import streamlit as st
import pickle
import pandas as pd
import requests





movies_list = pickle.load(open('movies.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))

movies = pd.DataFrame(movies_list)





def fetch_movie_poster(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=97bbb0232732688dbe0e0e86fbe1386f&language=en-US'.format(movie_id))

   data = response.json()
   print(data)
   return "https://image.tmdb.org/t/p/w500/"  +  data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x:x[1])[1:11]


    recom_movies = []
    recom_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recom_movies.append(movies.iloc[i[0]].title)
        recom_posters.append(fetch_movie_poster(movie_id))
    return recom_movies,recom_posters

st.title('Movie Recommender System')




selected_movie_name = st.selectbox(

    'Which movie You want to Select?',
    movies['title'].values
)



if st.button('Recommend'):

    recommended_movie_names , recommended_movie_posters = recommend(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col1:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

    with col3:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])    