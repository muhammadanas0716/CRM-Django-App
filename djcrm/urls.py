from django.contrib import admin
from django.urls import include, path


# Create your views here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
]
