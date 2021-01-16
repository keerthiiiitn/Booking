from django.shortcuts import render,redirect
from django.http import HttpResponse
from hotel.forms import user_registration,Roomdetails,BookRoom,Updation,ImgPfl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from booking import settings
from django.core.mail import send_mail
from django.contrib import messages
from hotel.models import Room_details,Book_Room,Upd

# Create your views here.

def home(request):
	return render(request,'hotel/home.html')

def register(request):
	if request.method == "POST":
		y = user_registration(request.POST)
		if y.is_valid():
			# p=y.save()
			p = y.save(commit=False)
			receiver = p.email
			sub = "Holiday Inn"
			msg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sender = settings.EMAIL_HOST_USER
			snt = send_mail(sub,msg,sender,[receiver])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(receiver))
				return redirect('/login')
			messages.danger(request,"please enter correct emailid or username or password")
	form = user_registration()
	return render(request,'hotel/register.html',{"form":form})

@login_required
def profile(request):
	return render(request,'hotel/profile.html')

@login_required
def update(request):
	if request.method == 'POST':
		c = Updation(request.POST,instance=request.user)
		y = ImgPfl(request.POST,request.FILES,instance=request.user.upd)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			messages.success(request,"{} your details updated successfully".format(request.user.username))
			return redirect("/profile")
	c = Updation(instance=request.user)
	y = ImgPfl(instance=request.user.upd)
	return render(request,'hotel/update.html',{'u':c,'q':y})
	


# @login_required
# def update(request):
# 	if request.method == 'POST':
# 		c = Updation(request.POST,instance=request.user)
# 		y = ImgPfl(request.POST,request.FILES,instance=request.user.upd)
# 		if c.is_valid() and y.is_valid():
# 			c.save()
# 			y.save()
# 			messages.success(request,"{} your details updated successfully".format(request.user.username))
# 			return redirect("/profile")
# 	c = Updation(instance=request.user)
# 	y = ImgPfl(instance=request.user.upd)
# 	return render(request,'dtlapp/updateprofile.html',{'u':c,'q':y})

@login_required
def rooms(request):
	x = Room_details.objects.all()
	rooms = []
	for i in x:
		if not Book_Room.objects.filter(room_no=i):
			rooms.append(i)
	return render(request,'hotel/rooms.html',{'rooms':rooms})

@login_required
def book_room(request,room):
	form = BookRoom(request.POST or None)
	if form.is_valid():
		t = form.save(commit=False)
		t.room_no = Room_details.objects.get(number=room)
		t.guest = request.user
		t.save()
		roomdetails = Room_details.objects.get(number=room)
		roomdetails.booked = True
		roomdetails.save()
		return redirect('/rooms')
	return render(request,'hotel/book_room.html',{'form':form})

@login_required
def myrooms(request,id):
	rooms = Book_Room.objects.filter(guest = request.user)
	return render(request,'hotel/myrooms.html',{'rooms':rooms})

def vacate(request,room):
	room = Book_Room.objects.filter(room_no = Room_details.objects.get(number=room))
	room.delete()
	return redirect('rooms')