from django.urls import path
from myapp.views import index, indexItem

app_name = "myapp"


urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name="detail"),
]