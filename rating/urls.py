from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('project/<int:id>', views.project, name='project'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('api/posts/', views.PostList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

