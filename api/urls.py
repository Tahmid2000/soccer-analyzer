from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('players/<str:pk>', views.players, name='api-overview')
]
