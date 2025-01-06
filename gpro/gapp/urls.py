from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('',views.login_user,name='login'),
    path('index',views.main,name='main'),
    path('add',views.add_user,name='add_user'),
    path('deletion/<int:id>',views.delete_g,name='deletion')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    
    
    
    
    
