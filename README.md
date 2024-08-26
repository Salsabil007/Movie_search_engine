## Movie Search Engine
It is a web-based application focusing on movies and user interaction with movie-related information. Specifically, the application will serve as a movie search engine 
for the users. In the movie search application, users could search for movies based on any combination of their preferences for genre, director, actor, and other attributes. 
They could also find the average rating for any movie. Additionally, users were able to add new movies and movie-related details to the database. The app required users to 
log in, and for those without an account, it provided the ability to create one, granting them access to the full features of the movie search engine.

### System Architecture:
Front end: HTML, CSS
Back End: Django, SQLite database
Language: Python, SQL

### Dataset: Users can add/modify movies and related information as well as add rating to movies. As the base dataset, we have used Movielens dataset which has a variety of
information about movies, including user ratings. Link: https://files.grouplens.org/datasets/hetrec2011/hetrec2011-movielens-readme.txt


### Database search: We have 12 different pages in the app that users can interact with. The movie detail page shows the detailed information of a movie including year, genre, 
average user rating, tags and actors associated with the movie given the name of a movie title. There are 9 different search pages where users can give a combination of 
criteria and the application shows the movies that satisfy the criteria. It includes search by actor, director, tag, actor and director pair etc. Users can insert a rating 
and find movies having average rating higher than or equal to that rating. Users can also insert a genre and year and find top 10 highly rated movies in that particular year 
and genre in descending order of their rating. The application also lets users do complex queries like finding movies of an actor within a timeframe where users insert the 
actor name and years. Also, users can search for lead actors and actresses associated with a movie selected by the user. 

### Adding or modifying database: The app lets the user add any movie and relevant information to the database. Based on the input of the users, the app also creates a new 
director if the specific director doesn’t exist in the database. Therefore, adding a movie updates the movie table as well as the director table. Users can also modify 
the information of a movie already existing in the database. When a user adds an existing movie again, it updates the instance of the movie in the database with the new 
information, but does not create multiple instances with the same title.  We also have an “add rating” page that lets an user give a rating to a specific movie or 
update his/her previously given rating.
