from django.urls import path
from . import views
#from .views import SearchPageView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('rate/', views.index2, name='index2'),
    #path('rate_double/', views.movie_awards, name='movie_awards'),
    path('search_by_director/', views.director_search_project, name='director_search_project'),
    path('search_by_actor/', views.actor_search_project, name='actor_search_project'),
    path('search_by_tag/', views.tag_search_project, name='tag_search_project'),
    path('search_by_rating/', views.rating_search_project, name='rating_search_project'),
    path('search_by_genre/', views.genre_search_project, name='genre_search_project'),
    path('test_add/', views.add_test, name='add_test'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path("search/",views.SearchPageView,name = "SearchPageView"),
    path('search_by_actor_and_genre/', views.actor_search_by_genre_project, name='actor_search_by_genre_project'), #DANIEL CHANGE
    path('search_by_actor_and_director/', views.actor_and_director_search_project, name='actor_and_director_search_project'), #DANIEL CHANGE
    path('search_lead_actors/', views.lead_actors_search_project, name='lead_actors_search_project'), #DANIEL CHANGE
    path('search_by_actor_between_years/', views.actor_search_between_years_project, name='actor_search_between_years_project'), #DANIEL CHANGE
]
