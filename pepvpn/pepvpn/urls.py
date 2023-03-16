from django.contrib import admin

from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vpn.urls')),
    path('about/', include('about.urls', namespace='about')),
]
