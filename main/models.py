from django.db import models
from django.db import models
from django.urls import reverse
from datetime import timedelta , date
from django.utils import timezone
     

class AnimeList(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    genre = models.TextField()
    episodes = models.IntegerField(default = 12)
    # image = models.ImageField(upload_to="pics")
    production = models.CharField(max_length=100)
    season = models.TextField( default="2021")
    premeire_date =models.TextField()
    anime_type = models.CharField(max_length=40,default="tv series")   
    discription = models.TextField()
    next_episode = models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('anime_index',kwargs={'my_id':self.anime_id})

