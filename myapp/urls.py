from django.urls import path
from myapp.views import *

app_name = "myapp"


urlpatterns = [
    path('', home, name='home'),
    path('<int:my_id>/', indexItem, name="detail"),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/<int:myid>/', profile_view, name='profile_view'),
    # path('logout/', logout_view, name='logout'),
]