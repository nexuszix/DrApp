# coding=utf8

from django.db import models
from django.utils import timezone

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class DrMas(models.Model):
	drCode = models.CharField(max_length=20, blank=True, default='')
	clinic = models.CharField(max_length=50, blank=True, default='')
	prefix = models.CharField(max_length=10, blank=True, default='คุณ')
	firstname = models.CharField(max_length=50, default='อภิมุข')
	lastname = models.CharField(max_length=50, default='ม่วง')
	specialty = models.CharField(max_length=50, blank=True, default='')
	locate = models.ForeignKey('Location', null=True, on_delete=models.SET_NULL)
	profile = models.TextField(blank=True, default='')
	schedule = models.TextField(blank=True, default='')
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)
	sun = models.BooleanField(default=False)
	lastedit = models.DateField(auto_now=True)
	editor = models.ForeignKey('auth.User')

	def __unicode__(self):
		return self.prefix + self.firstname + " " + self.lastname

class Location(models.Model):
	abrev = models.CharField(max_length=10)
	sname = models.CharField(max_length=20)
	fname = models.CharField(max_length=100)
	address = models.CharField(max_length=200)

	def __unicode__(self):
		return self.abrev



# Create your models here.
