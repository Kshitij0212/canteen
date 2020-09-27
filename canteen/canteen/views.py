from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'

class AboutUsPage(TemplateView):
    template_name = 'about_us.html'

class LoggedInPage(TemplateView):
    template_name = 'loggedin.html'
