from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Post
# Create your views he*
class HomeView(TemplateView):
    template_name = "home.html"

    #passa para o site as publicações
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] =  Post.objects.all().order_by('-created_date') #defininido pelo contrário da ordem de criação
        return context

