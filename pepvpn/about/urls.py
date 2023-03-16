from django.urls import path

from . import views


app_name = 'about'

urlpatterns = [
    path('download/', views.DownloadView.as_view(), name='download'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('donat/', views.DonatView.as_view(), name='donat'),
]
