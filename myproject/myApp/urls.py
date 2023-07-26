from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.Dashboards),
    path('stories/',views.stories),
    path('about/',views.about),
    path('',views.profile)
]