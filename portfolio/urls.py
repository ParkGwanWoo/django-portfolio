from django.urls import path
from . import views
app_name = "portfolio"

urlpatterns = [
    path("", view=views.index, name="index"),
]