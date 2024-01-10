from django.contrib import admin
from django.urls import include, path
from leads.views import LandingPageView


# Create your views here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('leads.urls', namespace='leads')),
]
