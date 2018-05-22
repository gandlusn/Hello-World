from django.conf.urls import url
from django.contrib import admin
from post import views
from django.conf.urls.static import static# this will allow us serve images
from django.conf import settings#to get to the informationin settings file

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.post_home,name='post_home'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post,name='post'),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#python manage.py runserver

