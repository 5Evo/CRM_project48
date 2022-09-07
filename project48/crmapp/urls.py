"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from crmapp import views

app_name = 'crmapp'

urlpatterns = [
    path('', views.main_view),
    path('index/', views.main_view, name='index'),
    path('lead_list/', views.LeadListView.as_view(), name='leads'),
    path('lead_card/<int:pk>/', views.LeadDetailView.as_view(), name='lead_card'),
    path('create_lead/', views.LeadCreateView.as_view(), name='create_lead'),
    path('lead_update/<int:pk>/', views.LeadUpdateView.as_view(), name='lead_update'),
    path('lead_delete/<int:pk>/', views.LeadDeleteView.as_view(), name='lead_delete'),
    path('charts/', views.charts_view, name='charts'),
    path('tables/', views.tables_view, name='tables'),
    path('buttons/', views.buttons_view, name='buttons'),
    path('cards/', views.cards_view, name='cards'),
    path('blank/', views.blank_view, name='blank'),
    path('register/', views.register_view, name='register'),
    path('utilities-color/', views.utilities_color_view, name='utilities-color'),
    path('index_original/', views.main_view_original, name='index_original'),
]
