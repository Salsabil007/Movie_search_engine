from django.shortcuts import render
from .forms import DirectorForm, MovieDirectorForm,ActorForm, TagForm, RatingForm, GenreForm, Addmovieform, LeadActorsForm, ActorBetweenYearsForm, ActorAndGenreForm, ActorAndDirectorForm,testform
from .models import  Movieproject, Directorproject, Actorproject, Featuresproject, Tagproject, Taggedasproject, Watchedbyproject, Director, Movie2
from django.db.models import Avg
from django.views.generic import TemplateView,ListView

from django.db import connection ##new line
'''
def index(request):
    form = DirectorForm()
    movies = None
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            
            director_name = form.cleaned_data['name']
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT a.title FROM movies_movie2 a WHERE a.director = %s
                """,[director_name])
                movies = cursor.fetchall()

    return render(request, 'movies/index.html', {'form': form, 'movies': movies})


def index2(request):
    form = DirectorForm()
    movies = None
    average_rating = None
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director_name = form.cleaned_data['name']
            movies = Movie2.objects.filter(director=director_name)
            average_rating = movies.aggregate(Avg('imdb_rating'))['imdb_rating__avg']
            #average_rating = movies.aggregate(Avg('imdb_rating'))

    return render(request, 'movies/index2.html', {'form': form, 'movies': movies, 'average_rating': average_rating})

def movie_awards(request):
    form = MovieDirectorForm()
    rating = None
    if request.method == 'POST':
        form = MovieDirectorForm(request.POST)
        if form.is_valid():
            director_name = form.cleaned_data['director']
            movie_title = form.cleaned_data['movie']
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT a.imdb_rating FROM movies_movie2 a WHERE a.director = %s AND a.title = %s 
                """,[director_name, movie_title])
                rating = cursor.fetchall()


    return render(request, 'movies/rating2.html', {'form': form, 'rating': rating})
'''

def director_search_project(request):
    form = DirectorForm()
    movies = None
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            
            director_name = form.cleaned_data['name']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    Select m.title,d.directorName from movies_movieproject m inner join movies_directorproject d on m.directorID = d.directorID where d.directorName = %s
                """,[director_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_director.html', {'form': form, 'movies': movies})

def actor_search_project(request):
    form = ActorForm()
    movies = None
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            
            actor_name = form.cleaned_data['name']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    Select m.title,a.actorName from movies_movieproject m, movies_featuresproject f, movies_actorproject a where a.actorID = f.actorID and f.movieID=m.movieID and a.actorName = %s
                """,[actor_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_actor.html', {'form': form, 'movies': movies})

def tag_search_project(request):
    form = TagForm()
    movies = None
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            
            tag_name = form.cleaned_data['name']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    Select m.title,t.tagName from movies_movieproject m, movies_tagproject t, movies_taggedasproject tt where t.tagID = tt.tagID and tt.movieID=m.movieID and t.tagName = %s
                """,[tag_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_tag.html', {'form': form, 'movies': movies})


def rating_search_project(request):
    form = RatingForm()
    movies = None
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            
            rating = form.cleaned_data['name']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    Select m.title from movies_movieproject m where m.movieID in (select movieID from movies_watchedbyproject group by movieID having avg(rating) > %s)                 
                """,[rating])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_rating.html', {'form': form, 'movies': movies})


def genre_search_project(request):
    form = GenreForm()
    movies = None
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    Select m.title, avg(b.rating) AS avg_raing FROM movies_movieproject m JOIN movies_watchedbyproject b ON m.movieID = b.movieID where m.genre = %s and m.year = %s GROUP BY m.movieID ORDER BY avg_raing DESC LIMIT 10                 
                """,[name,year])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_genre.html', {'form': form, 'movies': movies})

def add_movie(request):
    msg = " "
    dir = None
    form = Addmovieform()
    if request.method == 'POST':
        form = Addmovieform(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            aa = Movieproject.objects.filter(title=title)
            if len(aa) > 0:
                mv, created = Movieproject.objects.get_or_create(title = title)
            else:

            #mv, created = Movieproject.objects.get_or_create(title = title)
                mv = Movieproject(title=title)
            if form.cleaned_data['directorID']:
                a = Directorproject.objects.filter(directorName=form.cleaned_data['directorID'])
                if len(a) > 0:
                    dir = a[0].directorID
                else:
                    d, created2 = Directorproject.objects.get_or_create(directorName = form.cleaned_data['directorID'], directorID = str(Directorproject.objects.count() + 1))
                    #d.directorID = str(Directorproject.objects.count() + 1)
                    d.save()
                    dir = d.directorID

            '''if not created:
                mv.year = form.cleaned_data['year'] or mv.year
                mv.imdbPictureURL = form.cleaned_data['imdbPictureURL'] or mv.imdbPictureURL
                mv.genre = form.cleaned_data['genre'] or mv.genre
                mv.AddressSpace1 = form.cleaned_data['AddressSpace1'] or mv.AddressSpace1
                mv.AddressSpace2 = form.cleaned_data['AddressSpace1'] or mv.AddressSpace2
                if form.cleaned_data['directorID']:
                    mv.directorID = dir or mv.directorID
            else:
                mv.movieID = 54978 + Movieproject.objects.count() + 1
                mv.year = form.cleaned_data['year'] or mv.year
                mv.imdbPictureURL = form.cleaned_data['imdbPictureURL'] or mv.imdbPictureURL
                mv.genre = form.cleaned_data['genre'] or mv.genre
                mv.AddressSpace1 = form.cleaned_data['AddressSpace1'] or mv.AddressSpace1
                mv.AddressSpace2 = form.cleaned_data['AddressSpace2'] or mv.AddressSpace2
                if form.cleaned_data['directorID']:
                    mv.directorID = dir or mv.directorID'''
            if len(aa) > 0:
                mv.year = form.cleaned_data['year'] or mv.year
                mv.imdbPictureURL = form.cleaned_data['imdbPictureURL'] or mv.imdbPictureURL
                mv.genre = form.cleaned_data['genre'] or mv.genre
                mv.AddressSpace1 = form.cleaned_data['AddressSpace1'] or mv.AddressSpace1
                mv.AddressSpace2 = form.cleaned_data['AddressSpace1'] or mv.AddressSpace2
                if form.cleaned_data['directorID']:
                    mv.directorID = dir or mv.directorID
            else:
                mv.movieID = 54978 + Movieproject.objects.count() + 1
                mv.year = form.cleaned_data['year'] 
                mv.imdbPictureURL = form.cleaned_data['imdbPictureURL'] 
                mv.genre = form.cleaned_data['genre'] or mv.genre
                mv.AddressSpace1 = form.cleaned_data['AddressSpace1'] 
                mv.AddressSpace2 = form.cleaned_data['AddressSpace2'] 
                if form.cleaned_data['directorID']:
                    mv.directorID = dir or mv.directorID
            
            '''if form.cleaned_data['tagName']:
                a = Tagproject.objects.filter(tagName=form.cleaned_data['tagName'])
                if len(a) == 0:
                    t, created3 = Tagproject.objects.get_or_create(tagName = form.cleaned_data['tagName'], tagID = 16529+Tagproject.objects.count() + 1)
                    t.save()'''
            mv.save()
            
            msg = "Successful update!"
    return render(request, 'movies/movie_add.html', {'form': form, 'msg': msg})


def SearchPageView(request):
    return render(request, 'movies/search.html')


def actor_and_director_search_project(request): #Daniel Addition
    form = ActorAndDirectorForm()
    movies = None
    if request.method == 'POST':
        form = ActorAndDirectorForm(request.POST)
        if form.is_valid():
            
            director_name = form.cleaned_data['director']
            actor_name = form.cleaned_data['actor']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT m.title, d.directorName, a.actorName FROM movies_movieproject m JOIN movies_directorproject d ON m.directorID = d.directorID JOIN movies_featuresproject f ON m.movieID = f.movieID JOIN movies_actorproject a ON f.actorID = a.actorID WHERE d.directorName = %s AND a.actorName = %s
                """,[director_name, actor_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_actor_and_director.html', {'form': form, 'movies': movies})

def actor_search_between_years_project(request): #Daniel addition
    form = ActorBetweenYearsForm()
    movies = None
    if request.method == 'POST':
        form = ActorBetweenYearsForm(request.POST)
        if form.is_valid():
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            actor_name = form.cleaned_data['actor']
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT M.year, M.title FROM movies_movieproject M JOIN movies_featuresproject F ON M.movieID = F.movieID JOIN movies_actorproject A ON F.actorID = A.actorID WHERE (M.year BETWEEN %s AND %s) AND A.actorName = %s;
                """,[start_year, end_year, actor_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_actor_between_years.html', {'form': form, 'movies': movies})

def lead_actors_search_project(request):#DANIEL addition
    form = LeadActorsForm()
    actors = None
    if request.method == 'POST':
        form = LeadActorsForm(request.POST)
        if form.is_valid():
            
            movie_name = form.cleaned_data['movie']
            
            # '''
            # try:
            #     director = Director.objects.get(name=director_name)
            #     movies = director.movies.all()
            # except Director.DoesNotExist:
            #     movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                               SELECT a.actorName FROM movies_movieproject m JOIN movies_featuresproject f ON m.movieID = f.movieID JOIN movies_actorproject a ON f.actorID = a.actorID WHERE m.title = %s ORDER BY f.actorRankInMovie LIMIT 5;

                """,[movie_name])
                result = cursor.fetchall()
                actors = [row[0] for row in result]
    
    return render(request, 'movies/lead_actors_by_movie.html', {'form': form, 'actors': actors})
#DANIEL ADDITION
def actor_search_by_genre_project(request):
    form = ActorAndGenreForm()
    movies = None
    if request.method == 'POST':
        form = ActorAndGenreForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            actor_name = form.cleaned_data['name']
            
            '''
            try:
                director = Director.objects.get(name=director_name)
                movies = director.movies.all()
            except Director.DoesNotExist:
                movies = []'''
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT m.title, m.genre FROM movies_movieproject m JOIN movies_featuresproject f ON m.movieID = f.movieID JOIN movies_actorproject a ON f.actorID = a.actorID WHERE m.genre = %s AND a.actorName = %s
                """,[genre, actor_name])
                movies = cursor.fetchall()
    
    return render(request, 'movies/movie_by_actor_and_genre.html', {'form': form, 'movies': movies})



#Select m.title from movies_movieproject m where m.directorID = %s


def add_test(request):
    msg = " "
    form = testform()
    if request.method == 'POST':
        form = testform(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            mv, created = Movie2.objects.get_or_create(title = title)
            if not created:
                mv.director = form.cleaned_data['director'] or mv.director
                mv.imdb_rating = form.cleaned_data['imdb_rating'] or mv.imdb_rating
            else:
                mv.director = form.cleaned_data['director']
                mv.imdb_rating = form.cleaned_data['imdb_rating']
            mv.save()
            msg = "Successful update!"
    return render(request, 'movies/test_add.html', {'form': form, 'msg': msg})
    
