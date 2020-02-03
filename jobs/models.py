from django.db import models

# Create your models here.
class Job(models.Model):
	#Images
	image = models.ImageField(upload_to='images/')
	#summary 
	summary = models.CharField(max_length=200)
	app_name = models.CharField(max_length=200)

	#
	date_published = models.DateField('date published')
	site_url = models.CharField(max_length=200)


	def __str__(self):
		return self.app_name