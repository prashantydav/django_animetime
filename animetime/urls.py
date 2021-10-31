
from django.contrib import admin
from django.urls import path 
from main.views import  index_view,create_view , dynamic_view  , anime_news_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('news/',anime_news_view , name = 'news'),
    path('',index_view,name='anime_index'),
    path('create/',create_view,name='anime_create'),
    path('index/<int:my_id>/',dynamic_view,name='anime_index'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
