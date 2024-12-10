from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.PostView.as_view(), name='postview')
    
]