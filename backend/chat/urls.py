from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

from chat.forms import CustomUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('api:index')
        ),
        name='registration'
    ),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('api.urls')),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)