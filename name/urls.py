from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name="sourav"),
    path('reg',views.reg,name="reg"),
    path('logi',views.logi,name="logi"),
    path('logout',views.logout,name="logout"),
    path('cv',views.cvv,name="cv"),
    path('ccv',views.ccv,name="ccv"),
    path('mass',views.mass,name="mass"),
    path('newmass',views.newmass,name='new')
]
