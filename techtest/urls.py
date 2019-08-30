from django.urls import include, path
# Urls
urlpatterns = [
    path('', include('api.urls')),
]