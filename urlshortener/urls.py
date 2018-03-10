from django.urls import path

from . import views

handler404 = 'views.handler404'

urlpatterns = [

    path('', views.index, name='index'),

    path('l/<slug:link_code>/', views.detail, name='detail'),

    path('save-link/', views.save_link, name='save-link')
]