from django.db import models

# Create your models here.

# Structure of our model ->

# NEWS ->
# 	> Title 
# 	> Summary
# 	> Source 
# 	> URL
# 	> published_at


class NewsArticle(models.Model):
	
	title = models.CharField(max_length=255)
	description = models.TextField()
	source = models.CharField(max_length=400)
	url = models.URLField(max_length=400)
	published_at = models.DateTimeField()


	def __str__(self):
		return self.title

 