from django.urls import path
from .views import homepage,character_list,detail,games

urlpatterns = [
    path('',homepage,name='home'),
    path('characters/',character_list,name='character_list'),
    path('detail/',detail,name='detail'),
    path('games/', games, name='games'),
]