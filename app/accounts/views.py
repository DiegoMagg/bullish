from accounts.forms import RegisterForm
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views import View


class RegisterView(View):
    template = 'register.html'

    def get(self, request):
        form = RegisterForm(request.GET or None)
        return render(request, self.template, locals())

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, self.template, locals())
