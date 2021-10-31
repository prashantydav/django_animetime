from django.shortcuts import render ,redirect
from .models import AnimeList
from .forms import AnimeForm 
from animetime.mixins import ScrapedData , save_data
from django.contrib import messages
    
       
anime_data= ScrapedData
save_data(anime_data)

def anime_news_view(request):
    data = ScrapedData
    news = data.get_news()
    
    context = {
        "news":news
    }
    return render(request,'news.html',context)


    

def index_view(request):
    obj = AnimeList.objects.all()
    sea = obj[0].season
    
    print(obj , obj[0].season)
    
    context = {
        "obj":obj,
        'sea': sea
    }
    return render(request, 'index.html',context)

def dynamic_view(request,my_id):
    obj = AnimeList.objects.get(anime_id=my_id)
    
    

    context = {
        'obj':obj
        
    }
    return render(request,'details.html',context)

# def loginview(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username = username , password = password)

#         if user is not None:
#             login(request , user)
#             return redirect('/')
#         else:
#             messages.error(request,'wrong username or password')
#             return redirect('login')

#     return render(request , "login.html" , {})   


def create_view(request):
    form = AnimeForm(request.POST or None)


    if form.is_valid():
        form.save()

    else:
        messages.error(request,f'{form.errors}')

    form = AnimeForm()
    context = {
        'form':form
    }
    return render(request,'create.html',context)

# def logoutview(request):
#     logout(request)
#     return redirect('login')

