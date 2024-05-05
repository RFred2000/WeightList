from django.urls import path

from . import views

app_name = "info"
urlpatterns = [
    path("about", views.about, name="about")
]