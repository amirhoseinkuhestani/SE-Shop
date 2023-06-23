from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "shop"

urlpatterns = [
    path('', home, name="home"),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('signup/', signup,name='signup'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('create_ticket/', create_ticket, name='create_ticket'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)