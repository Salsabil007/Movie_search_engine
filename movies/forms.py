from django import forms
from django.forms import ModelForm, TextInput
from .models import Movieproject, Movie2

class DirectorForm(forms.Form):
    name = forms.CharField(label='Director Name', max_length=200)

class ActorForm(forms.Form):
    name = forms.CharField(label='Actor Name', max_length=200)

class TagForm(forms.Form):
    name = forms.CharField(label='Tag Name', max_length=200)

class RatingForm(forms.Form):
    name = forms.FloatField(label='Rating')

class GenreForm(forms.Form):
    name = forms.CharField(label='Genre', max_length=200)
    year = forms.IntegerField(label="Year")


class MovieDirectorForm(forms.Form):
    director = forms.CharField(label='Director Name', max_length=200)
    movie = forms.CharField(label='Movie Name', max_length=200)

class Addmovieform(forms.ModelForm):
    #tagName = forms.CharField(max_length=200)
    class Meta:
        model = Movieproject
        fields = ['title', 'year', 'imdbPictureURL','genre','AddressSpace1','AddressSpace2','directorID']
        widgets = {
            "title": TextInput(attrs={'required':True}),
            #"tagName": TextInput(attrs={'required':False}),
        }

class LeadActorsForm(forms.Form): #Daniel Addition
    movie = forms.CharField(label='Movie Name', max_length=200)

class ActorBetweenYearsForm(forms.Form): #daniel Addition
    actor = forms.CharField(label='Actor Name', max_length=200)
    start_year = forms.CharField(label='Start Year', max_length=200)
    end_year = forms.CharField(label='End Year', max_length=200)
class ActorAndGenreForm(forms.Form): #Daniel addition
    name = forms.CharField(label='Actor Name', max_length=200)
    genre = forms.CharField(label='Genre', max_length=200)

class ActorAndDirectorForm(forms.Form): #daniel Addition
    actor = forms.CharField(label='Actor Name', max_length=200)
    director = forms.CharField(label='Director Name', max_length=200)

'''class testform(forms.Form):
    director = forms.CharField(label='Director Name', max_length=200)
    title = forms.CharField(label='Movie Name', max_length=200)
    imdb_rating = forms.FloatField(label = "Imdb rating")'''


class testform(forms.ModelForm):
    class Meta:
        model = Movie2
        fields = ['title', 'director', 'imdb_rating']
        widgets = {
            "title": TextInput(attrs={'required':True}),
            "director": TextInput(attrs={'required':False}),
        }


