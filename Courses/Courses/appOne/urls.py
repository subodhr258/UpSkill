from django.urls import path
from appOne import views

urlpatterns = [
path('courses/',views.courses,name='courses'),
path('aboutus/',views.aboutus,name='aboutus'),
path('',views.index,name='index'),
path('contact/',views.contact,name='contact'),
]
