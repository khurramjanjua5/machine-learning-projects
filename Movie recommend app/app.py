import pickle
import streamlit as st
import requests
import pickle

def fetch_poster(movie_id):
    response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=38a063b8650328b7e68e98e562e339e7&language=en-US".format(movie_id)
)
    data= response.json()

    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]]['title'])
        # Access 'title' column here
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

movies = pickle.load(open('movies.pkl', 'rb'))
# Assuming the structure of the DataFrame loaded from 'movies.pkl' is as follows:
# Columns: ['movie_id', 'title', 'tags']
movies_list = movies['title'].values  # Accessing 'title' column here

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list)

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])



import gzip
import pickle

# Specify the filename of the pickle file to compress
pickle_filename = 'similarity.pkl'

# Specify the filename for the compressed pickle file
compressed_pickle_filename = 'similar.pkl.gz'

# Load the data from the pickle file
with open(pickle_filename, 'rb') as f:
    data = pickle.load(f)

# Compress the data and write it to a gzip-compressed file
with gzip.open(compressed_pickle_filename, 'wb') as f:
    pickle.dump(data, f)

print("Pickle file compressed successfully.")
