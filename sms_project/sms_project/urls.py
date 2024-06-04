from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from smsapp.views import ulogin, usignup, uhome, ulogout, ucp, create, remove

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", uhome, name="home"),
    path("ulogin/", ulogin, name="ulogin"),
    path("usignup/", usignup, name="usignup"),
    path("ulogout/", ulogout, name="ulogout"),
    path("ucp/", ucp, name="ucp"),
    path("create/", create, name="create"),
    path("remove/<int:id>/", remove, name="remove"),
]