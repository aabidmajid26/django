from django.urls import path,include
from . import views




urlpatterns = [
    path("", views.home, name="home"),
    path("people/", views.showAll, name="people"),
    path("add/", views.add, name="add"),
    path("people/<int:p_id>/", views.showPerson,name="person")
]