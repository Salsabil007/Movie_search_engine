from django.db import models

class Director(models.Model):                   #dummy model
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):                      #Dummy model
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
    
class Movie2(models.Model):                     #Dummy model
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    imdb_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Movieproject(models.Model):
    movieID = models.IntegerField(primary_key=True)
    imdbPictureURL = models.CharField(max_length=300,null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200,null=True, blank=True)
    genre = models.CharField(max_length=200,null=True, blank=True)
    AddressSpace1 = models.CharField(max_length=200,null=True, blank=True)
    AddressSpace2 = models.CharField(max_length=200,null=True, blank=True)
    directorID = models.CharField(max_length=100,null=True, blank=True)
    

    def __str__(self):
        return self.title
    
    '''def __str__(self):
        return self.genre
    
    def __str__(self):
        return self.AddressSpace1

    def __str__(self):
        return self.AddressSpace2'''
    
class Directorproject(models.Model):
    directorID = models.CharField(max_length=100,primary_key=True)
    directorName = models.CharField(max_length=200,null=True, blank=True)
    

    def __str__(self):
        return self.directorName
    
class Actorproject(models.Model):
    actorID = models.CharField(max_length=100,primary_key=True)
    actorName = models.CharField(max_length=200,null=True, blank=True)
    

    def __str__(self):
        return self.actorName
    
class Featuresproject(models.Model):
    movieID = models.IntegerField()
    actorID = models.CharField(max_length=100)
    actorRankInMovie = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('movieID', 'actorID')
        constraints = [
            models.UniqueConstraint(fields=['movieID', 'actorID'], name='unique_id1_id2')
        ]

    '''def __str__(self):
        return f"{self.id1}-{self.id2} on {self.device}"'''
    
class Tagproject(models.Model):
    tagID = models.IntegerField(primary_key=True)
    tagName = models.CharField(max_length=200,null=True, blank=True)
    

    def __str__(self):
        return self.tagName
    
class Taggedasproject(models.Model):
    movieID = models.IntegerField()
    tagID = models.IntegerField()
    tagweight = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('movieID', 'tagID')
        constraints = [
            models.UniqueConstraint(fields=['movieID', 'tagID'], name='unique_movieid1_tagid2')
        ]

class Watchedbyproject(models.Model):
    movieID = models.IntegerField()
    userID = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('movieID', 'userID')
        constraints = [
            models.UniqueConstraint(fields=['movieID', 'userID'], name='unique_movieid1_userid2')
        ]
