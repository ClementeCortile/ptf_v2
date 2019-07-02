from django.urls import path

from . import views

urlpatterns = [
    path('', views.allCode, name='allcode'),
    path('<int:code_id>/', views.detailcode, name='detailcode'),
    path('note1', views.musicchallange, name='musicchallange'),
    path('note2', views.codechallange, name='codechallange'),
    path('note3', views.galileo, name='galileo')

]