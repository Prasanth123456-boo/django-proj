from . import views
from django.urls import path
urlpatterns = [
    
    path('',views.view),
    path('create/',views.create),
    path('<id>',views.viewbyid)
]
