from django.urls import path

from .views import (home, lead_create, lead_delete, lead_detail, lead_list,
                    lead_update)

app_name = 'leads'

urlpatterns = [
    path('', home, name='home'),
    path('leads/', lead_list, name='list'),
    path('create/', lead_create, name='create'),
    path('<int:pk>/update/', lead_update, name='update'),
    path('<int:pk>/delete/', lead_delete, name='delete'),
    path('<int:pk>/', lead_detail, name='detail'),
]
