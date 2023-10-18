"""
URL configuration for projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectsapps import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>/',views.Studentget.as_view()),
    path('student/<int:pk>/',views.Studentget.as_view()),
    path('student/',views.Studentpost.as_view()),
    # path('student/',views.Studentput.as_view()),
    path('student/<int:pk>/',views.Studentput.as_view()),
    path('student/',views.studentpatch.as_view()),
    # path('studentdelete/',views.studentdelete.as_view()),
    path('student/<int:pk>/', views.studentdelete.as_view()),
    path('course/',views.courseget.as_view()),
    path('course/<int:pk>/',views.courseget.as_view()),
    path('course/',views.coursepost.as_view()),
    path('course<int:pk>/',views.courseput.as_view()),
    path('course<int:pk>/',views.coursepatch.as_view()),
    path('course/<int:pk>/',views.coursepost.as_view()),
    # path('coursedelete/',views.coursedelete.as_view()),
     path('coursedelete/<int:pk>/', views.coursedelete.as_view()),
]
