from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('r1s.html', TemplateView.as_view(template_name="r1s.html"), name='r1s'),
    path('r1t.html', TemplateView.as_view(template_name="r1t.html"), name='r1t'),
    path('r2.html', TemplateView.as_view(template_name="r2.html"), name='r2'),
    path('r3.html', TemplateView.as_view(template_name="r3.html"), name='r3'),
    path('registration.html', TemplateView.as_view(template_name="registration.html"), name='registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

