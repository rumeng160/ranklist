from django.conf.urls import url
from .views import addrank,lookrank
urlpatterns = [
    url(r'addrank',addrank),
    url(r'lookrank',lookrank),

]