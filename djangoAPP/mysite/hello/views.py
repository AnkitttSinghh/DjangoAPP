from django.http import HttpResponse

def home(request):
    return HttpResponse("Learn DevOps with Ankit")
