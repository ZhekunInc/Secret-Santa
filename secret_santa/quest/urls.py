from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='quest/homepage.html',
            get_context_data=lambda: {'is_home_page': True}
        ),
        name='home_page'
    ),
]
