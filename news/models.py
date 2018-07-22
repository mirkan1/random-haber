from django.db import models

class NewsItem(models.Model):
	title = models.CharField(max_length=255)
	date_creation = models.DateTimeField(auto_now_add=True)
	date_publish = models.DateTimeField(blank=True, null=True)
	#author = models.ForeignKey(settings.)
	content = models.TextField()

	def __str__(self):
		return self.title