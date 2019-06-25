from django.urls import path

from . import views

app_name = 'CMdiagnose'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create1/', views.NewDetailView.as_view(), name='newdetail'),
    path('createy/', views.NewDetailYao.as_view(), name='newdetailyao'),
    path('new/', views.newPerson, name='new'),
    path('newy/', views.newYao, name='newy'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/resultsy/', views.ResultsYao.as_view(), name='resultsy'),
    path('<int:person_id>/tell/', views.tell, name='tell'),
]