from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseall.urls')),
    path('api/', include('baseall.api.urls'))
]
 