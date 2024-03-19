# Music Recommender System

A content based music recommender system using cosine similarity

This Python script creates a movie recommender system accessible through a user-friendly web interface built with Streamlit. The system leverages precomputed movie data and similarity scores, loaded using the pickle library. Upon launching the interface, users are presented with a dropdown menu containing a list of movie titles to choose from. Upon selecting a movie and clicking the "Show Recommendations" button, the system asynchronously calculates and displays the top five recommended movies based on similarity scores to the chosen movie. The recommendations are presented alongside their corresponding movie posters fetched from the TMDb API using asynchronous HTTP requests managed by asyncio and aiohttp.

The code's architecture demonstrates efficient utilization of asynchronous programming techniques, enhancing the system's responsiveness and scalability. By employing asyncio and aiohttp for asynchronous operations, the script seamlessly integrates with Streamlit, enabling real-time interaction with the recommender system while efficiently fetching movie posters. The user interface is intuitive, allowing users to effortlessly explore movie recommendations based on their preferences, thereby enhancing their overall movie-watching experience
