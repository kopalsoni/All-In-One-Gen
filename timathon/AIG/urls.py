from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path("", views.home, name="home"),
                path("about", views.about, name="about"),
                path("image_gen", views.image_gen, name="image_gen"),
                path("music_gen", views.music_gen, name="music_gen"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
