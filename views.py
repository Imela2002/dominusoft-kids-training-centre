from http.client import HTTPResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from app.models import News
from app.models import ProgramCategory
from app.models import Program
from app.models import ContactMessage
from unicodedata import category


# CRUD
# Create
# Read
# Update
# Delete


#MyProject views

def rreth_nesh(request):
    return render(request, 'rreth nesh.html')

def kryefaqja(request):
    categories = ProgramCategory.objects.all()
    return render(request, 'kryefaqja.html', {'categories': categories})

def kontaktet(request):
    return render(request, 'kontaktet.html')

def news1(request):
    return render(request, 'news1.html')

def news2(request):
    return render(request, 'news2.html')

def news3(request):
    return render(request, 'news3.html')

def news4(request):
    return render(request, 'news4.html')

def programi1(request):
    return render(request, 'programi1.html')

def programi2(request):
    return render(request, 'programi2.html')

def programi3(request):
    return render(request, 'programi3.html')

def programi4(request):
    return render(request, 'programi4.html')


def blogu(request):
   news = News.objects.all()
   return render(request, 'blogu.html', {"news_data": news})

def viewnews(request, news_nr):
    news = News.objects.get(id=news_nr)
    return render(request, "viewnews.html", {"viewnews": news})


from django.shortcuts import render, get_object_or_404
from .models import ProgramCategory, ContactMessage


def program_categories_view(request):
    categories = ProgramCategory.objects.all()
    return render(request, 'kryefaqja.html', {'categories': categories})

def programs_by_category_view(request, category_id):
    category = get_object_or_404(ProgramCategory, id=category_id)
    programs = category.programs.all()
    return render(request, 'programs.html', {'category': category, 'programs': programs})

from .forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse

def kontaktet(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'kontaktet.html', {'form': form})

def success(request):
    return HttpResponse('Success!')

