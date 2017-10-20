from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from boxer.models import Profile

class SputnikView(TemplateView):
    template_name = "landing.html"
    def post(self,request):
        values = request.POST.dict()
        del values['csrfmiddlewaretoken']
        Freighter.objects.create(**values)
        return redirect('/thanks')

class ThanksPageView(TemplateView):
    template_name = "thanks.html"
