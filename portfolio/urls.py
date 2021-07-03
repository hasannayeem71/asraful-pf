from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('message/',views.msg,name="msg"),
    path('delete/<int:m_id>', views.delete,name="delete"),
]
