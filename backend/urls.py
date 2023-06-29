from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import api

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', api.signup, name="signup"),
    path('login/', api.login, name="login"),
    path('logout/', api.logout, name="logout"),
    path('is-superuser/<int:id>/', api.issuperuser, name="is-superuser"),

    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
