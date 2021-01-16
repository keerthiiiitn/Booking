from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	l = [('English','English'),('Hindi','Hindi'),('Telugu','Telugu'),('Urdhu','Urdhu')] 
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	lang = models.CharField(max_length=10,choices=l)
	address = models.CharField(max_length=200,null=True)
	phno = models.CharField(max_length=10,null=True)
	impf = models.ImageField(upload_to="Profile/",default="avathar.png")

class Upd(models.Model):
	g = [('M','Male'),('F','Female')]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7, choices=g)
	im = models.ImageField(upload_to="Profile_pics/",default="avathar.jpg")
	p = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def Createpfl(sender,instance,created,**kwargs):
	if created:
		Upd.objects.create(p=instance)

class Room_details(models.Model):
	tp=[('AC','AC'),('NON-AC','NON-AC')]
	cat=[('Double Bed','Double Bed'),('Single Bed','Single Bed'),('Triple Bed','Triple Bed')]
	number = models.IntegerField(default=101,unique=True)
	room_type = models.CharField(max_length=12,choices=tp)
	category = models.CharField(max_length=10,choices=cat)
	cost = models.IntegerField(default=2000)
	image = models.ImageField(upload_to="Image/",default="avathar.png")

	def __str__(self):
		return str(self.number)


class Book_Room(models.Model):
    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room_no = models.ForeignKey(Room_details, on_delete = models.CASCADE)
    persons = models.IntegerField()
    guest = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.guest.username