from django.db import models

# Create your models here.
class Signup(models.Model):
	email = models.EmailField()
	full_name = models.CharField(default = "type", max_length = 2000, null = True)
	timestamp = models.DateTimeField(auto_now_add= True,auto_now = False)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return self.email


