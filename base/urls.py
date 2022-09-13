
from django.contrib import admin
from django.urls import path, include
from landing import urls
from dashboard import urls


from django.conf.urls.static import static #import setting
from django.conf import settings # Import Settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('', include('dashboard.urls'))



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media file configuration in url
