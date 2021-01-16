from django.urls import path
from hotel import views
from django.contrib.auth import views as v 

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',v.LoginView.as_view(template_name="hotel/login.html"),name="login"),
    path('logout/',v.LogoutView.as_view(template_name="hotel/logout.html"),name="logout"),
    path('rooms/',views.rooms,name='rooms'),
    path('profile/',views.profile,name="pfl"),
    path('update/',views.update,name="upd"),
    path('book_room/<int:room>/',views.book_room,name="book_room"),
    path('myrooms/<int:id>/',views.myrooms,name="myrooms"),
    path('vacate/<int:room>',views.vacate,name='vacate'),
]
