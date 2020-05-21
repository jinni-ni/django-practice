from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:qudstion_id>/',views.dtail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:qudstion_id>/vote/', views.vote, name='vote'),
]
