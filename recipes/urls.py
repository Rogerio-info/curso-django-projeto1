from django.urls import path
#from recipes import views
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),

]
