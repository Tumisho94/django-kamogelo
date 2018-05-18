from django.db import models

RATING = (
	(1,'Poor'),
	(2,'Average'),
	(3,'Good'),
	(4,'Very good'),
	(5,'Excellent')
)
# Create your models here.
class Recipe(models.Model):
	title                = models.CharField(max_length = 50)
	prep_time            = models.CharField(max_length = 20, blank = True)
	cooking_time         = models.CharField(max_length = 20, blank = True)
	serves               = models.CharField(max_length = 100)
	ingredients          = models.TextField(max_length = 1000)
	cooking_instructions = models.TextField(max_length = 1000)
	image                = models.FileField(upload_to = 'recipe')


class Rating(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	rate   = models.IntegerField(choices = RATING)
