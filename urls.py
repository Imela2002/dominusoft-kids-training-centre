"""
URL configuration for djangoProject2 project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from app.views import kryefaqja, rreth_nesh, blogu, kontaktet, news1, news2, news3, news4, programi1, programi2, programi3, viewnews, programs_by_category_view, program_categories_view, success
from djangoProject2 import settings

#MyProject urls

urlpatterns = [
    path('', kryefaqja),
    path('admin/', admin.site.urls),
    path('rrethnesh/', rreth_nesh),
    path('kryefaqja/', kryefaqja),
    path('blogu/', blogu),
    path('kontaktet/', kontaktet),
    path('news1/', news1),
    path('news2/', news2),
    path('news3/', news3),
    path('news4', news4),
    path('programi1/', programi1),
    path('programi2/', programi2),
    path('programi3/', programi3),
    path('news/<int:news_nr>/', viewnews),
    path('categories/', program_categories_view, name='categories'),
    path('category/<int:category_id>/programs/', programs_by_category_view, name='programs_by_category'),
    path('success/', success, name='success'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
