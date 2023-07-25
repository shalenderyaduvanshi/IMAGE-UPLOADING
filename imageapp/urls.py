from . import views
from django.urls import path

urlpatterns=[
    path('',views.IndexPage, name='index'),
    path('upload/', views.UploadImage, name='imageupload'),
    path('showimg/', views.ImageFetch, name='show')

]