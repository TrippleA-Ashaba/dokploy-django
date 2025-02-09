from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "doktest/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["python_version"] = "3.12"
        context["django_version"] = "5.1.6"
        return context
