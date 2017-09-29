from django.db import models

# Create your models here.

# 发布会表
class Event(models.Model):
	name = models.CharField(max_length=100)
	limit = modles.IntegerField()
	status = modles.BooleanFiled()
	address = modles.CharField(max_length=200)
	start_time = modles.DateTimeField('events time')
	creatr_time = modles.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

#嘉宾表
class Guest(models.Model):
	

		

		
